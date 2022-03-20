from django.shortcuts import render, redirect
import datetime
from datetime import datetime
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import *
from .forms import *
from nlp_component.models import *
from django.conf import settings
from django.db.utils import OperationalError
from nlp_component.feedback_handling.main_process import *
from django.utils.translation import activate


def change_language(request):
    if request.method == 'POST':
        language_form = LanguageForm(request.POST)
        language = request.POST.get('language')
        if language == "en":
            activate("en")
        if language == "de":
            activate("de")
    else:
        language_form = LanguageForm()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def index(request):
    """Rendering the first html-page that shows all error categories for the currently active instance"""
    instance = Instance.objects.get(currently_active=True)
    error_categories = ErrorCategory.objects.filter(instance=instance.id)
    error_appearances = ErrorAppearance.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'user_site/index.html',
        {
            'error_categories': error_categories,
            'error_appearances': error_appearances,
            'title': 'Error category',
            'date': datetime.now().date,
        }
    )


def error_appearance(request, location):
    """Rendering the html-page that shows all error appearances that belong to the previously selected error category"""
    assert isinstance(request, HttpRequest)
    instance = Instance.objects.get(currently_active=True)
    locations = [Location.objects.get(id=location)]

    error_appearances = ErrorAppearance.objects.filter(locations=location)
    return render(
        request,
        'user_site/error_appearance.html',
        {
            'error_appearances': error_appearances,
            'locations': locations,
            'title': 'Error appearance',
            'date': datetime.now().date,
        }
    )


def pdf_locations(request, location):
    """Rendering a extra pop-up window that shows the pdf-document belonging to a previously selected error location"""
    location_object = Location.objects.get(id=location)
    pdf_document = location_object.pdf_document
    instance = Instance.objects.get(currently_active=True)
    locations = Location.objects.filter(instance=instance.id)
    print(pdf_document)
    return render(
        request,
        'user_site/location_pdfs.html',
        {
            'instance': instance,
            'pdf_document': pdf_document,
            'locations': locations,
            'title': 'PDF Dokument',
            'location': location_object,
            'date': datetime.now().date,
        }
    )


def solution(request):
    """endering the html-page that shows all solution that belong to the previously selected error appearance"""
    solutions = []
    locations = []
    instance = Instance.objects.get(currently_active=True)
    user_comment_form = UserCommentForm()
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            error_appearance = ErrorAppearance.objects.get(id=request.POST.get('err_app'))
            locations = error_appearance.locations.all()
            solutions = Solution.objects.filter(error_appearance=request.POST.get('err_app'))

    else:
        form = SolutionForm()
    return render(
        request,
        'user_site/solution.html',
        {
            'solutions': solutions,
            'locations': locations,
            'user_comment_form': user_comment_form,
            'title': 'Solution',
            'date': datetime.now().date,
        }
    )


def rating(request):
    """if a user rated a solution positively/negatively its rating increases/decreases by 1"""
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            sol = Solution.objects.get(pk=request.POST.get('sol'))
            if "positive" in request.POST:
                sol.rating += 1
            else:
                sol.rating -= 1
            sol.save()
    else:
        form = RatingForm()
    return redirect('index')


def user_comment(request):
    """starting the nlp-component process to process a user comment (new solution proposal)"""
    if request.method == 'POST':
        user_comment_form = UserCommentForm(request.POST)
        if user_comment_form.is_valid():
            content = request.POST.get('content')
            print(request.POST.get('err_app'))
            err_app = ErrorAppearance.objects.get(pk=request.POST.get('err_app'))
            process_user_comment(user_comment=content, error_appearance=err_app)
    else:
        comment_form = UserCommentForm()
    return redirect('index')


def search_process(request):
    """rendering the html-page that shows all error appearances/solutions that exist and contain the search word(s)"""
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_area = request.POST.get('search_area')
            search_field = request.POST.get('search_field')
            instance = Instance.objects.get(currently_active=True)
            locations = Location.objects.filter(instance=instance.id)
            if search_area == 'error_appearance':
                error_appearances = ErrorAppearance.objects.filter(name__icontains=search_field,
                                                                   error_category__instance=instance.id)
                return render(
                    request,
                    'user_site/error_appearance.html',
                    {
                        'error_appearances': error_appearances,
                        'title': 'Error appearance',
                        'date': datetime.now().date,
                    }
                )
            elif search_area == 'solution':
                solutions = Solution.objects.filter(name__icontains=search_field,
                                                    error_appearance__error_category__instance=instance.id)
                user_comment_form = UserCommentForm()
                return render(
                    request,
                    'user_site/solution.html',
                    {
                        'solutions': solutions,
                        'user_comment_form': user_comment_form,
                        'title': 'Solution',
                        'date': datetime.now().date,
                        'search_process': True,
                    }
                )

    else:
        return redirect('index')