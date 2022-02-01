from django import forms
from . import models

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        fields = ('title', 'xls',)