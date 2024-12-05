from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


from django.contrib.auth.views import PasswordResetDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView
from django.shortcuts import redirect

from django.urls import reverse_lazy


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



    



class CustomPasswordResetView(PasswordResetView):
    # You can customize the form class or template here
    template_name = 'accounts/custom_password_reset_form.html'  # Your custom form template
    email_template_name = 'accounts/custom_password_reset_email.html'  # Your custom email template
    subject_template_name = 'accounts/custom_password_reset_subject.txt'  # Optional: Custom subject

    # Optionally, override the success URL to redirect after the form submission
    success_url = reverse_lazy('password_reset_done')  # Redirect here after form submission




class CustomPasswordResetDoneView(PasswordResetDoneView):


    template_name = 'accounts/password_reset_done.html'  # Your custom confirm template

    def get_redirect_url(self):
        # Redirect the user to the home page or any other URL after the reset email is sent
        return reverse_lazy('login')  # 'home' is the name of your home page URL
    


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    # You can customize the template here if you wish
    template_name = 'accounts/custom_password_reset_confirm.html'  # Your custom confirm template
    
    # Optionally, override form validation or other behaviors
    success_url = reverse_lazy('password_reset_complete')  # Redirect here after password reset



class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/custom_password_reset_complete.html'  # Your custom complete template



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  # Redirect to the profile page
    else:
        form = CustomUserCreationForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})
