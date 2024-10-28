
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import FoodItem

from django.views.generic.edit import DeleteView

from django.views.generic import ListView

from .forms import FoodItemForm


class CreateFoodItemView(View):
    def get(self, request):
        form = FoodItemForm()
        return render(request, 'food_items/create_food_item.html', {'form': form})

    def post(self, request):
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_items_management')
        else:
            print("form error",form.errors)
        return render(request, 'food_items/create_food_item.html', {'form': form})


class EditFoodItemView(UpdateView):
    model = FoodItem
    form_class = FoodItemForm
    template_name = 'food_items/edit_food_item.html'
    context_object_name = 'food_items'

    def get_success_url(self):
        return reverse_lazy('food_items_management')


class DeleteFoodItemView(DeleteView):
    model = FoodItem
    template_name = 'food_items/confirm_delete.html'
    context_object_name = 'food_item'

    def get_success_url(self):
        return reverse_lazy('food_items_management')


class DisplayFoodItemsView(ListView):
    model = FoodItem
    template_name = 'food_items/display_food_items.html'
    context_object_name = 'food_items'
