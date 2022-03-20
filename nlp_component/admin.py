from django.contrib import admin
from django.shortcuts import render
from django.urls import path

import user_site.admin
from .models import *
from django.utils.translation import ugettext_lazy as _
from user_site.admin import *
from .forms import *
from .feedback_handling.main_process import *
# Register your models here.


class FeedbackAdminSite(admin.AdminSite):
    """custom admin site for the user comments"""
    site_header = _("Comment management")
    site_title = _("Comment management")
    index_title = _("Comment management")

    def get_urls(self):
        urls = super(FeedbackAdminSite, self).get_urls()
        custom_urls = [
            path('admin/create_solution/<int:group_id>', self.admin_view(create_solution), name="create_solution"),
            path('admin/save_new_solution/<int:group_id>', self.admin_view(save_new_solution), name="save_new_solution"),
        ]
        return custom_urls + urls


feedback_app_admin_site = FeedbackAdminSite(name="feedback_admin")


def get_group_data(group_id):

    data = []
    sentences = Sentence.objects.filter(group_id=group_id)
    for sentence in sentences:
        user_comment = UserComment.objects.get(pk=sentence.user_comment_id)
        user_comment_sentences = []
        for user_comment_sentence in Sentence.objects.filter(user_comment=user_comment):
            if user_comment_sentence == sentence:
                user_comment_sentences.append((user_comment_sentence, 1))
            else:
                user_comment_sentences.append((user_comment_sentence, 0))

        keywords = Keyword.objects.filter(sentence=sentence)
        keywords_lemmas = [keyword.lemma for keyword in keywords]

        data.append([user_comment_sentences, ", ".join(keywords_lemmas)])
        print(data)
    return data


def create_solution(request, group_id):
    """"""

    title = _("Create new solution")
    group = CommentGroup.objects.get(pk=group_id)
    error_appearance = group.error_appearance.name
    data = get_group_data(group_id)
    group_represent = get_group_represent(group_id)
    create_solution_form = CreateSolutionForm(initial={'error_appearance': error_appearance, 'name': group_represent,
                                                       'description': group_represent, 'rating': 0})
    return render(
        request,
        'admin/create_solution.html',
        {
            'title': title,
            'group_id': group_id,
            'has_permission': True,
            'data': data,
            'create_solution_form': create_solution_form,
        }
    )


def save_new_solution(request, group_id):
    group = CommentGroup.objects.get(pk=group_id)
    if request.method == 'POST':
        create_solution_form = CreateSolutionForm(request.POST)
        if create_solution_form.is_valid():
            name = request.POST.get('name')
            description = request.POST.get('description')
            media = request.POST.get('media')
            rating = request.POST.get('rating')

            solution = Solution(name=name, description=description,
                                rating=rating, error_appearance=group.error_appearance)
            if media:
                solution.media = media
            solution.save()
    else:
        create_solution_form = CreateSolutionForm()

    return HttpResponseRedirect('../../' + CommentGroup._meta.app_label + '/' +
                                CommentGroup._meta.model_name + '/' + str(group_id) + '/change')


@admin.register(UserComment, site=feedback_app_admin_site)
class UserCommentAdmin(admin.ModelAdmin):
    """showing the user comments at the admin site"""
    list_display = ("content", "error_appearance")


@admin.register(CommentGroup, site=feedback_app_admin_site)
class CommentGroupAdmin(admin.ModelAdmin):
    """showing the groups at the admin site"""

    change_form_template = "admin/group_template.html"
    list_display = ("get_name", "error_appearance", "get_amount_user_comments")
    readonly_fields = ("error_appearance",)

    def get_name(self, obj):
        return _("Group") + " " + str(obj.id)

    def get_amount_user_comments(self, obj):
        return len(Sentence.objects.filter(group_id=obj.id))

    get_name.short_description = _("Group of user comments")
    get_amount_user_comments.short_description = _("Amount of user comments")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}

        data = get_group_data(object_id)

        extra_context['data'] = data

        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )


# models that dont need to be seen

@admin.register(Threshold, site=feedback_app_admin_site)
class ThresholdAdmin(admin.ModelAdmin):
    list_display = ("value",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

"""
@admin.register(Sentence, site=feedback_app_admin_site)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ("content",)


@admin.register(Keyword, site=feedback_app_admin_site)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ("lemma",)
"""