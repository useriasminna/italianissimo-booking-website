"""
Menu App - Views
----------------
Views for Menu App.
"""
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from menu.models import Favourite, Meal
from menu.forms import SetFavourite


class Menu(ListView):
    """
    A view that provides meals data and a form to create entries for Favourite
    """

    template_name = "menu.html"
    model = Favourite

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['menu_list'] = Meal.objects.all()
        context['favourite_form'] = SetFavourite
        context['favourites'] = Favourite.objects.all()

        return context

    def post(self, request):
        """Override post method"""
        if request.method == 'POST':

            favourite_form = SetFavourite(data=request.POST)

            if favourite_form.is_valid():
                meal_id = favourite_form.cleaned_data['meal_id']
                user = request.user
                meal = get_object_or_404(Meal, pk=meal_id)
                favourite = Favourite(user=user, meal=meal,)
                favourite.save()

                return HttpResponseRedirect('/menu')

            return HttpResponseRedirect('/menu')

        favourite_form = SetFavourite(request.GET)
        return render(request, 'menu.html', {'favourite_form': favourite_form, })

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
