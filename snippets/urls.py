from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('snippets/cat/<int:pk>', views.LanguageView.as_view(), name='language'),
    path('snippets/user/juancito/', views.user_snippets, name='user_snippets'),
    path('snippets/<int:pk>', views.SnippetDetailView.as_view(), name='snippet'),
    path('snippets/add/', views.AddSnippetView.as_view(), name='snippet_add'),
    path('snippets/edit/<int:pk>', views.SnippetUpdateView.as_view(), name='snippet_edit'),
    path('snippets/delete/<int:pk>', views.SnippetDeleteView.as_view(), name='snippet_delete'),
]