from . import views
from django.urls import path

urlpatterns = [
    path('createbookings/', views.Booking.as_view(), name='booking'),
    path('profile/', views.BookingList.as_view(), name='booking_list'),
    path('profile/booking/<int:pk>/remove/', views.BookingDeleteView.as_view(), name='booking_remove')
]