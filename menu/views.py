from django.views.generic import ListView
from menu.forms import addFavourite
from menu.models import Favourite, Meal
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from italianissimo.decorators import customer_required, staff_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# Create your views here.
class Menu(ListView):
    template_name = "menu.html"
    model = Favourite

    def get_context_data(self,*args, **kwargs):
        context = super(Menu, self).get_context_data(*args,**kwargs)
        context['menu_list'] = Meal.objects.all()
        context['favourite_form'] = addFavourite
        context['favourites'] = Favourite.objects.all()
        
        return context
    
    @method_decorator(customer_required, name='dispatch') 
    def post(self, request):
        
        if request.method=='POST':
            
            favourite_form = addFavourite(data=request.POST)             
            
            if favourite_form.is_valid():
                meal_id = favourite_form.cleaned_data['meal_id']           
                user = request.user
                meal = get_object_or_404(Meal , pk=meal_id)
                favourite = Favourite(user = user, meal=meal,)
                favourite.save()
                
                return HttpResponseRedirect('/menu') 
            else:
                return HttpResponseRedirect('/menu') 
        else:
            favourite_form = addFavourite(request.GET) 
        
        return render(request, 'menu.html', {'favourite_form': favourite_form,})
    
@method_decorator(customer_required, name='dispatch')    
class FavouriteDeleteView(DeleteView, LoginRequiredMixin):
    model = Favourite
    success_url = reverse_lazy('menu')
    template_name = 'menu.html'