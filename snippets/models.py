from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Language(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    slug = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name



class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True)
    snippet = RichTextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language', blank=False, null=False)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

