from django.shortcuts import redirect
# menu/views.py
from django.views.generic import TemplateView
from menu.views import Menu
from fooditems.views import FoodItem


# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Menu.objects.all()  # Pass all categories to the template
#         return context


# class SpecialHomeView(TemplateView):
#     template_name = 'special_home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = FoodItem.objects.all()  # Pass all categories to the template
#         return context
    


class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

# class ContactUsView(TemplateView):
#     template_name = 'contact_us.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
