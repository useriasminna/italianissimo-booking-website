from django.views.generic import TemplateView


# Create your views here.
class Booking(TemplateView):
    template_name = "booking.html"