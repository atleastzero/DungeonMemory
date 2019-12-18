from django.urls import path

from . import views

urlpatterns = [
    path('', views.CharactersSavedListView.as_view(), name='characters-saved-list'),
]