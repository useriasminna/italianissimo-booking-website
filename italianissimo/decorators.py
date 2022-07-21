# Import Django messages
from django.contrib import messages
from django.http import HttpResponseRedirect

# Custom Decorator
def staff_required(function):
    def _function(request, *args, **kwargs):
        if not request.user.staff:
            messages.info(request, "Sorry, this content is restricted")
            return HttpResponseRedirect('/bookings/profile/')
        return function(request, *args, **kwargs)

    return _function

def customer_required(function):
    def _function(request, *args, **kwargs):
        if request.user.staff:
            messages.info(request, "Sorry, this content is restricted")
            return HttpResponseRedirect('/bookings/managebookings/')
        return function(request, *args, **kwargs)

    return _function