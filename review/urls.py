from . import views
from django.urls import path

urlpatterns = [
    path('addreview/', views.Review.as_view(), name='add_review'),
    
    
]