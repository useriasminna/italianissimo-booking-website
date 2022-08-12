from django.views.generic import ListView
from menu.forms import addFavourite
from menu.models import Favourite, Meal
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# Create your views here.
class Menu(ListView):
    
    """
    A view that provides meals data and a form to create entries for Favourite 
    """
    
    template_name = "menu.html"
    model = Favourite

    def get_context_data(self,*args, **kwargs):
        context = super(Menu, self).get_context_data(*args,**kwargs)
        context['menu_list'] = Meal.objects.all()
        context['favourite_form'] = addFavourite
        context['favourites'] = Favourite.objects.all()
        
        return context
     
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
    
    # def get(self, *args, **kwargs):
    #     return redirect('menu')
    
class FavouriteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    
    """
    A view that deletes a Favourite entry from the database. 
    The action is performed only if the authenticated user is the author of Favourite entry.
    """
    
    model = Favourite
    success_url = reverse_lazy('menu')
    template_name = 'menu.html'
    
    def test_func(self):
        item = self.get_object()
        return self.request.user == item.user