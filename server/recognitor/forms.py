from django import forms
from django.forms import ModelForm

from .models import AudioUploadFile


class AudioUploadForm(ModelForm):
    class Meta:
        model = AudioUploadFile
        fields = ('audioFile',)
        widgets = {
            "audioFile": forms.FileInput(
                attrs={
                    "class": "form-control form-control-lg",
                }
            )
        }
