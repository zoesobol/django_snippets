from django import forms
from . import models

class SnippetForm(forms.ModelForm):
    class Meta:
        model = models.Snippet
        fields =['name', 'description', 'language', 'public', 'snippet']