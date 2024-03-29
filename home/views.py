"""
Home App - Views
----------------
Views for Home App
"""

from django.views.generic import ListView
from django.db.models import Count
from django.db.models.functions import Length

from menu.models import Favourite, Meal
from review.models import Review
from users.models import User


class Home(ListView):
    """
    A view that provides filtered reviews and meals data
    """
    template_name = "index.html"
    model = Review

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['review_list'] = Review.objects.annotate(review_len=Length(
                                'review_text')).filter(
                                 review_len__lte=400).order_by('-rate')
        context['meals'] = Meal.objects.all()
        context['fav'] = Favourite.objects.values('meal_id').annotate(
                        meal_count=Count('meal_id')).order_by('-meal_count')
        context['users'] = User.objects.all()
        return context
