from datetime import date, datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from .models import Review as ReviewModel
from django.contrib import messages
from review.forms import newReviewForm
from django.http import HttpResponse, HttpResponseRedirect
import time



# Create your views here.
class Review(LoginRequiredMixin, TemplateView):

    template_name = "reviews.html"
    model = ReviewModel
    form_class = newReviewForm
    
    def get_context_data(self,*args, **kwargs):
        context = super(Review, self).get_context_data(*args,**kwargs)
        context['review_form'] = newReviewForm      
        return context
    
    def post(self, request):
        
        if request.method=='POST':
            
            review_form = newReviewForm(data=request.POST)             
            
            if review_form.is_valid():
                rate = review_form.cleaned_data['rate']
                if rate:
                    rateValue=rate
                else:
                    rateValue=1     
                text =review_form.cleaned_data['review_text']               
                user = request.user
                 
                review = ReviewModel(rate = rateValue, review_text = text, author = user,)
                review.save()
                messages.success(request, 'Your review was successfully added to the list')
                return HttpResponseRedirect('/reviews/addreview/') 
            
            else:
                messages.error(request, 'There was a problem submiting your review. Please try again!')
                return HttpResponseRedirect('/reviews/addreview/') 
        else:
            review_form = newReviewForm(request.GET) 
        
        return render(request, 'booking.html', {'review_form': review_form,})