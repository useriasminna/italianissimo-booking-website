from . import views
from django.urls import path

urlpatterns = [
    path('', views.Contact.as_view(), name='contact'),
]