from user_site.forms import *
from django.urls import reverse
from django.utils.translation import get_language


def language_form_context_processor(request):
    return {
        'language_form': LanguageForm(initial={'language': get_language()}),
    }


def search_form_context_processor(request):
    return {
        'search_form': SearchForm(),
    }


def instance_processor(request):
    instance = Instance.objects.get(currently_active=True)
    return {
        'instance': instance
    }


def locations_processor(request):
    instance = Instance.objects.get(currently_active=True)
    locations = Location.objects.filter(instance=instance.id)
    return {
        'locations': locations
    }
