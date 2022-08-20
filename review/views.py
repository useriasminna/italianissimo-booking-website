"""
Review App - Views
----------------
Views for Review App.
"""
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from review.forms import ReviewForm
from users.models import User
from .models import Review as ReviewModel


class Review(ListView):
    """
    A view that provides the list of reviews and also a form for creating Review entries
    """

    template_name = "reviews.html"
    model = ReviewModel
    form_class = ReviewForm
    context_object_name = "review_list"
    paginate_by = 4

    def get_queryset(self):
        return ReviewModel.objects.order_by('-date_updated_on')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['review_form'] = ReviewForm
        context['reviews'] = ReviewModel.objects.all()
        context['users'] = User.objects.all()
        return context

    def post(self, request):
        """Override post method"""
        if request.method == 'POST':

            review_form = ReviewForm(data=request.POST)

            if review_form.is_valid():
                rate = review_form.cleaned_data['rate']
                if rate:
                    rate_value = rate
                else:
                    rate_value = 1
                text = review_form.cleaned_data['review_text']
                user = request.user

                review = ReviewModel(rate=rate_value, review_text=text, author=user,)
                review.save()
                messages.success(request, 'Your review was successfully added to the list')
                return HttpResponseRedirect('/reviews')

            messages.error(request, 'There was a problem submiting your review.'\
                                    'Please try again!')
            return HttpResponseRedirect('/reviews')

        review_form = ReviewForm(request.GET)
        return render(request, 'reviews.html', {'review_form': review_form, })


class ReviewUpdate(UserPassesTestMixin, UpdateView):
    """
    A view that provides a form to update the Review entry coresponding to the authenticated user
    """

    model = ReviewModel
    template_name = "reviews.html"
    success_url = ('/reviews')

    fields = ['rate', 'review_text']

    def post(self, request, pk):

        review = get_object_or_404(ReviewModel, pk=pk)
        if request.method == 'POST':

            review_form = ReviewForm(data=request.POST, instance=review)

            if review_form.is_valid():
                review_form.instance.date_updated_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                review = ReviewModel()
                review_form.save()
                messages.success(request, 'Your review was successfully updated')
                return HttpResponseRedirect('/reviews')

            messages.error(request, 'There was a problem when trying to update'\
                                    'your review.Please try again!')
            return HttpResponseRedirect('/reviews')

        return render(request, 'reviews.html', {'review_form': review_form, })

    def test_func(self):
        item = self.get_object()
        return self.request.user == item.author
