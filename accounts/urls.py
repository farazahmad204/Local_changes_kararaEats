# accounts/urls.py

from django.urls import path
from .views import RegisterView, CustomLoginView
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetDoneView,CustomPasswordResetView,CustomPasswordResetConfirmView,CustomPasswordResetCompleteView,edit_profile
from . import views

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),


    # Custom Password Reset URLs
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),



    path('profile/', views.edit_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
