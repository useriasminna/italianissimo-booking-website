from . import views
from django.urls import path

urlpatterns = [
    path('/booking', views.Booking.as_view(), name='booking'),
]