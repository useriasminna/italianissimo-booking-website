from . import views
from django.urls import path

urlpatterns = [
    path('', views.Review.as_view(), name='reviews'),
    path('review/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review_update'),
    
    
]