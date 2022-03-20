from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *


class CreateSolutionForm(forms.Form):

    error_appearance = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
            'class': 'vTextfield virtualKeyboard',
            'id': 'id_error_appearance',
            'readonly': True,
        }),
        label=_("Error appearance")+":")

    name = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
            'class': 'vTextfield virtualKeyboard',
            'id': 'id_name',
        }),
        label=_("Name")+":")

    description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
            'class': 'vTextfield virtualKeyboard',
            'id': 'id_description',
        }),
        label=_("Description")+":")

    media = forms.FileField(widget=forms.ClearableFileInput(attrs={
            'class': '',
            'id': 'id_media',
        }),
        label=_("Image/Video")+":", required=False)

    rating = forms.IntegerField(widget=forms.NumberInput(attrs={
            'class': 'vIntegerField',
            'id': 'id_rating',
        }),
        label=_("Rating")+":")