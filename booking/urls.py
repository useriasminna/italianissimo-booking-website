from . import views
from django.urls import path

urlpatterns = [
    path('createbookings/', views.Booking.as_view(), name='booking'),
]