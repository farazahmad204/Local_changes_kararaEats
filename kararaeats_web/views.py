from django.shortcuts import redirect
# menu/views.py
from django.views.generic import TemplateView

from accounts.models import  CustomUser



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
    

def is_manager(user):
    """
    Check if the logged-in user exists in the Accounts table with the username 'Kool'.
    """
    try:
        # Query the Accounts table (CustomUser model) for the username 'Kool'
        return CustomUser.objects.filter(username='fahm', password=user.password).exists()
    except CustomUser.DoesNotExist:
        return False
# class ContactUsView(TemplateView):
#     template_name = 'contact_us.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
