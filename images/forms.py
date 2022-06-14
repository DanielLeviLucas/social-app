from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        modle = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }
