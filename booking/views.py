from django.views.generic import TemplateView
from .forms import newBookingForm
from django.shortcuts import render


# Create your views here.
class Booking(TemplateView):
    template_name = "booking.html"
    
    def post(self, request, slug, *args, **kwargs):
        

    #     # booking_form = newBookingForm(data=request.POST)

    #     # if booking_form.is_valid():
    #     #     booking_form.instance.email = request.user.email
    #     #     booking_form.instance.name = request.user.username
    #     #     booking = booking_form.save(commit=False)
    #     #     booking.save()
    #     # else:
    #     #     booking_form = newBookingForm()    

        return render(
            request,
            "booking.html",
            {
                'booking_form': newBookingForm()
            })