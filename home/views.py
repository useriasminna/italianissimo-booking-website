from django.views.generic import TemplateView, ListView
from django.db.models import Q
from review.models import Review 
from users.models import User
from django.db.models.functions import Length

# Create your views here.
class Home(ListView):
    template_name = "index.html"
    model = Review

    def get_context_data(self,*args, **kwargs):
        context = super(Home, self).get_context_data(*args,**kwargs)
        context['review_list'] = Review.objects.annotate(review_len=Length('review_text')).filter(review_len__lte=400).order_by('-rate')
        context['users'] = User.objects.all() 
        return context