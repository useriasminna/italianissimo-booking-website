from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Contact(TemplateView):
    
    """
    A view that only loads the contact html template
    """
    template_name = "contact.html"