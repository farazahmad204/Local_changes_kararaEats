from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages
from .forms import CustomUserCreationForm


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f"Account created for {username}")
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect a particular user to a different home page
        if self.request.user.username == 'mohsin.ijaz@outlook.com':  # Replace 'special_user' with the specific username
            return reverse('display_menu')
        return reverse('WeeklyMenu')  # Redirect to the default home page


# Login view (class-based)
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True  # Redirect logged-in users if they try to access the login page

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.info(self.request, f"You are now logged in as {username}")
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect a particular user to a different home page
        if self.request.user.username == 'fahm':  # Replace 'special_user' with the specific username
            return reverse('display_menu')
        return reverse('WeeklyMenu')  # display_menu_user Redirect to the default home page
