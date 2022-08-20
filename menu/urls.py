"""
Menu App - URLS
----------------
Urls Configuration for Menu App.
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Menu.as_view(), name='menu'),
    path('favourite/<int:pk>/remove/', views.FavouriteDeleteView.as_view(),
         name='favourite_remove'),
]
