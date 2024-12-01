from PIL.ImageShow import DisplayViewer
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from kararaeats_web.views import is_manager
from .models import FoodItem

from django.views.generic.edit import DeleteView

from django.views.generic import ListView

from .forms import FoodItemForm


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.views import View
from .forms import FoodItemForm
from .models import FoodItem

@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
@method_decorator(user_passes_test(is_manager, login_url=reverse_lazy('login')), name='dispatch')
class CreateFoodItemView(View):
    def get(self, request):
        form = FoodItemForm()
        return render(request, 'food_items/create_food_item.html', {'form': form})

    def post(self, request):
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.created_by = request.user  # Save the user who created the item
            food_item.save()
            return redirect('food_items_management')
        else:
            print("form error", form.errors)
        return render(request, 'food_items/create_food_item.html', {'form': form})

@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
@method_decorator(user_passes_test(is_manager, login_url=reverse_lazy('login')), name='dispatch')
class EditFoodItemView(UpdateView):
    model = FoodItem
    form_class = FoodItemForm
    template_name = 'food_items/edit_food_item.html'
    context_object_name = 'food_items'
    def get_success_url(self):
        return reverse_lazy('food_items_management')

@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
@method_decorator(user_passes_test(is_manager, login_url=reverse_lazy('login')), name='dispatch')
class DeleteFoodItemView(DeleteView):
    model = FoodItem
    template_name = 'food_items/confirm_delete.html'
    context_object_name = 'food_item'
    def get_success_url(self):
        return reverse_lazy('food_items_management')

@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
@method_decorator(user_passes_test(is_manager, login_url=reverse_lazy('login')), name='dispatch')
class DisplayFoodItemsView(View):
    model = FoodItem
    template_name = 'food_items/display_food_items.html'
    context_object_name = 'food_items'

    def get(self, request):
        food_items = self.model.objects.all()
        return render(request, self.template_name, {self.context_object_name: food_items})
"""
class DisplayFoodItemsView(DisplayViewer):
    model = FoodItem
    template_name = 'food_items/display_food_items.html'
    context_object_name = 'food_items'

    @user_passes_test(is_manager, login_url=reverse_lazy('login'))
    def get(self, request):
        return render(request, DisplayFoodItemsView.template_name, DisplayFoodItemsView.context_object_name)
"""