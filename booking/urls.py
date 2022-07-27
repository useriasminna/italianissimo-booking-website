from . import views
from django.urls import path

urlpatterns = [
    path('createbookings/', views.Booking.as_view(), name='booking'),
    path('profile/', views.BookingMealsList.as_view(), name='booking_list'),
    path('profile/booking/<int:pk>/remove/', views.BookingDeleteView.as_view(), name='booking_remove'),
    path('managebookings/', views.BookingListAdmin.as_view(), name='booking_list_admin'),
    path('managebookings/booking/<int:pk>/remove/', views.BookingDeleteViewAdmin.as_view(), name='booking_remove_admin'),
    
]