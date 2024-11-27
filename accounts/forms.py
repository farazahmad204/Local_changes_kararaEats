# accounts/forms.py

from django import forms
import re  # Import the re module for regular expressions
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    whatsapp_num = forms.CharField(max_length=15, required=True)
    address = forms.CharField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email','whatsapp_num', 'address']

    def clean_whatsapp_num(self):
        whatsapp_num = self.cleaned_data.get('whatsapp_num')

        # Regex pattern for validating Australian mobile numbers (e.g., +61 468 452067)
        pattern = r'^\+61\d{3}\d{6}$'

        # Check if the number matches the pattern
        if not re.match(pattern, whatsapp_num):
            raise forms.ValidationError("Please enter a valid mobile number in the format: +61XXXXXXXXX")

        # Check if the mobile number already exists in the database
        if CustomUser.objects.filter(whatsapp_num=whatsapp_num).exists():
            raise forms.ValidationError("A user with this mobile number already exists.")
        
        return whatsapp_num
    
    # Custom validation for the email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email address already exists.")
        return email
