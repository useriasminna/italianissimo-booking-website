"""
Contact App - Views
"""
from django.views.generic import TemplateView


class Contact(TemplateView):
    """
    A view that only loads the contact html template
    """
    template_name = "contact.html"
