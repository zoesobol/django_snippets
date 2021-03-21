from django import forms
from . import models

class SnippetForm(forms.ModelForm):
    class Meta:
        model = models.Snippet
        fields = ('user', 'name', 'description', 'language', 'public', 'snippet')
        widgets = {
            'user': forms.TextInput(attrs={'value':'', 'id':'author', 'type':'hidden'}),
            'snippet': forms.Textarea(attrs={'placeholder': 'Insertar snippet en la opción de "insertar snippet"'}),
        }
