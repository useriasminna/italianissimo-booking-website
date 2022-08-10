from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Contact(TemplateView):
    template_name = "contact.html"