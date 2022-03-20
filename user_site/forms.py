from django import forms
from import_export.forms import ImportForm, ConfirmImportForm
from django.utils.translation import ugettext_lazy as _
from .models import *
from django.utils.translation import get_language


class LanguageForm(forms.Form):
    SEARCH_AREAS = (
        ('en', _('English')),
        ('de', _('German')),
    )
    language = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-select mr-sm-2',
        }),
        initial=get_language(),
        choices=SEARCH_AREAS,
        label="Filter")


class MapCreatorForm(forms.Form):

    location_links = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'pop-addlink-input',
        }),
        label=_("Available locations"))

    def __init__(self, *args, **kwargs):
        locations = kwargs.pop('locations')
        location_links = (
            (str(location.pk), location.name) for location in locations)
        super(MapCreatorForm, self).__init__(*args, **kwargs)
        self.fields['location_links'].choices = location_links


class ImageMapForm(forms.Form):
    image_map = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': '',
            'id': 'final_image_map',
            'style': 'display:none',
            'type': 'hidden',
        }),
        label=False)


class SolutionForm(forms.Form):
    err_app = forms.IntegerField()


class RatingForm(forms.Form):
    sol = forms.IntegerField()


class AppearanceForm(forms.Form):
    location = forms.CharField(max_length=70)


class UserCommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control virtualKeyboard'
        }),
        label=_("Comment"))


class UploadForm(forms.Form):
    upload_file = forms.FileField(label=_("File"), widget=forms.ClearableFileInput(attrs={
        'class': 'form-control-file dropzone',
    }))

    def clean(self):
        cleaned_data = super(UploadForm, self).clean()
        upload_file = cleaned_data.get('upload_file')


class SearchForm(forms.Form):
    SEARCH_AREAS = (
        ('error_appearance', _('Error appearances')),
        ('solution', _('Solutions'))
    )
    search_area = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-select mr-sm-2',
        }),
        choices=SEARCH_AREAS,
        label="Filter")
    search_field = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Search'),
        })
    )


class ChangeInstanceForm(forms.Form):
    instance = forms.ModelChoiceField(queryset=Instance.objects.all())


class InstanceForm(forms.Form):
    instance = forms.ModelChoiceField(queryset=Instance.objects.all(), label=_("choose Instance"))


class ConfirmInstanceForm(forms.Form):
    instance = forms.ModelChoiceField(queryset=Instance.objects.all(), label=_("Choose Instance"))


class CompleteErrorImportForm(ImportForm):
    instance = forms.ModelChoiceField(queryset=Instance.objects.all(), required=True)


class CompleteErrorConfirmInputForm(ConfirmImportForm):
    instance = forms.ModelChoiceField(queryset=Instance.objects.all(), required=True)
