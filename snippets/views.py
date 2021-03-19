from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy

class IndexView(ListView):
    model = models.Snippet
    template_name = 'index.html'
    ordering = ['-id']


"""class LanguageView(ListView):
    model = models.Snippet
    template_name ='snippets/language_snippets.html'
    
    def get_queryset(self):
        language_name = self.request.GET('language')
        return models.Snippet.objects.all().filter(language__name = language_name)"""

"""def LanguageView(request, slug):
    language_snippets = models.Snippet.objects.filter(language__name = slug)
    return render(request, 'snippets/language_snippets.html', {'slug':slug, 'language_snippets':language_snippets})
"""

"""class LanguageView(ListView):
    model = models.Snippet
    template_name = 'snippets/language_snippets.html'

    def get_queryset(self):
        self.language = get_object_or_404(models.Language, pk=self.kwargs['pk'])
        return models.Snippet.objects.filter(language__name = self.language)
    
    def get_context_data(self, **kwargs):
        context = super(LanguageView, self).get_context_data(**kwargs)
        context['language'] = self.language
        return context"""

class LanguageView(ListView):
    model = models.Snippet
    template_name ='snippets/language_snippets.html'
    
    def get_queryset(self):
        qs= models.Snippet.objects.filter(public=True)
        language_name = self.request.GET.get('lang')
        if language_name:
            qs = qs.filter(language__name = language_name)
            
        return qs  


class SnippetDetailView(DetailView):
    model = models.Snippet
    template_name = 'snippets/snippet.html'


class AddSnippetView(CreateView):
    model = models.Snippet
    form_class = forms.SnippetForm
    template_name = 'snippets/snippet_add.html'

def user_snippets(request):
    return render(request, 'snippets/user_snippets.html', {})



class SnippetUpdateView(UpdateView):
    model = models.Snippet
    template_name = 'snippets/snippet_edit.html'
    form_class = forms.SnippetForm
    success_url = reverse_lazy('index')
   

class SnippetDeleteView(DeleteView):
    model = models.Snippet
    success_url = reverse_lazy('index')
    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)