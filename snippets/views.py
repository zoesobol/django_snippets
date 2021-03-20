from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy

class IndexView(ListView):
    model = models.Snippet
    template_name = 'index.html'
    ordering = ['-id']
    queryset = models.Snippet.objects.filter(public=True)


class LanguageView(ListView):
    model = models.Language
    template_name = 'snippets/language_snippets.html'

    def get_queryset(self):
        self.language = get_object_or_404(self.model, name=self.kwargs['language'])
        return models.Snippet.objects.filter(language__name=self.language.name)


class UserView(ListView):
    model = models.User
    template_name = 'snippets/user_snippets.html'

    def get_queryset(self):
        self.username = get_object_or_404(self.model, username=self.kwargs['username'])
        snippets = models.Snippet.objects.filter(user=self.username)

        if self.request.user.is_authenticated != False and str(self.request.user.username) != str(self.username):
            print(self.username)
            print(self.request.user.username)
            snippets = snippets.exclude(public = 'False')

        return snippets

class SnippetDetailView(DetailView):
    model = models.Snippet
    template_name = 'snippets/snippet.html'


class AddSnippetView(CreateView):
    model = models.Snippet
    template_name = 'snippets/snippet_add.html'
    form_class = forms.SnippetForm
    success_url = reverse_lazy('index')




class SnippetUpdateView(UpdateView):
    model = models.Snippet
    template_name = 'snippets/snippet_edit.html'
    form_class = forms.SnippetForm
    success_url = reverse_lazy('index')
   

class SnippetDeleteView(DeleteView):
    model = models.Snippet
    template_name = 'snippets/snippet_delete.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return models.Snippet.objects.filter(user=self.request.user)