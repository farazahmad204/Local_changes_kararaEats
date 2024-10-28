from django.views.generic import ListView
from django.shortcuts import render
from .forms import MenuForm
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from .models import Menu


class DisplayMenuView(ListView):
    model = Menu
    template_name = 'menu/display_menu.html'
    context_object_name = 'menus'


class DisplayUserMenuView(ListView):
    model = Menu
    template_name = 'menu/user_menu_display.html'
    context_object_name = 'menus'

    # Override get_context_data to customize context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Assuming each menu has related food_items
        ordered_menus = {}

        for menu in context['menus']:
            # For each menu, initialize the list of food items (empty for now)
            ordered_menus[menu] = []

        # Add this ordered_menus structure to the context for the template
        context['ordered_menus'] = ordered_menus
        return context


class CreateMenuView(View):
    def get(self, request):
        form = MenuForm()
        return render(request, 'menu/create_menu.html', {'form': form})

    def post(self, request):
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_menu')
        return render(request, 'menu/create_menu.html', {'form': form})


class EditMenuView(View):
    def get(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        form = MenuForm(instance=menu)
        return render(request, 'menu/edit_menu.html', {'form': form, 'menu': menu})

    def post(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('display_menu')
        return render(request, 'menu/edit_menu.html', {'form': form, 'menu': menu})


class DeleteMenuView(View):
    def post(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        menu.delete()
        return redirect('display_menu')


class MenuDashboardView(View):
    def get(self, request):
        menus = Menu.objects.all()  # Fetch all menus
        return render(request, 'menu/menu_dashboard.html', {'menus': menus})


# Weekly Menu view
def WeeklyMenuDisplay(request):
    menus = Menu.objects.all()  # Fetch all menus
    return render(request, 'menu/user_menu_weekly_display.html', {'menus': menus ,'user': request.user})
