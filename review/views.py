from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from users.models import User
from .models import Review as ReviewModel
from django.contrib import messages
from review.forms import newReviewForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
class Review(ListView):
    
    """
    A view that provides the list of reviews and also a form for creating Review entries
    """

    template_name = "reviews.html"
    model = ReviewModel
    form_class = newReviewForm
    context_object_name = "review_list"
    paginate_by = 4
    
    def get_queryset(self):
        return ReviewModel.objects.order_by('-date_updated_on') 
    
    def get_context_data(self,*args, **kwargs):
        context = super(Review, self).get_context_data(*args,**kwargs)
        context['review_form'] = newReviewForm 
        context['reviews'] = ReviewModel.objects.all()
        context['users'] = User.objects.all() 
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
                return HttpResponseRedirect('/reviews') 
            
            else:
                messages.error(request, 'There was a problem submiting your review. Please try again!')
                return HttpResponseRedirect('/reviews') 
        else:
            review_form = newReviewForm(request.GET) 
        
        return render(request, 'reviews.html', {'review_form': review_form,})
    
    
class ReviewUpdate(UserPassesTestMixin, UpdateView):
    
    """
    A view that provides a form to update the Review entry coresponding to the authenticated user
    """
    
    model = ReviewModel 
    template_name = "reviews.html"
    success_url = ('/reviews')
    
    fields = ['rate', 'review_text']
    
    def post(self, request, pk):
        
        review = get_object_or_404(ReviewModel , pk=pk)
        if request.method=='POST':
            
            review_form = newReviewForm(data=request.POST, instance=review)             
            
            if review_form.is_valid():
                review_form.instance.date_created_on = datetime.now()
                review_form.instance.date_updated_on = datetime.now()
                 
                review = ReviewModel()
                review_form.save()
                messages.success(request, 'Your review was successfully updated')
                return HttpResponseRedirect('/reviews') 
            
            else:
                messages.error(request, 'There was a problem submiting your review. Please try again!')
                return HttpResponseRedirect('/reviews') 
        
        return render(request, 'reviews.html', {'review_form': review_form,})
    
    def test_func(self):
        item = self.get_object()
        return self.request.user == item.author
    
