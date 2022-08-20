"""
Review App - URLS
----------------
URLS configuration for Review App.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Review.as_view(), name='reviews'),
    path('review/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review_update'),
]
