# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    whatsapp_num = forms.CharField(max_length=15, required=True)
    address = forms.CharField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'whatsapp_num', 'address']

    def clean_whatsapp_num(self):
        whatsapp_num = self.cleaned_data.get('whatsapp_num')
        if CustomUser.objects.filter(whatsapp_num=whatsapp_num).exists():
            raise forms.ValidationError("A user with this mobile number already exists.")
        return whatsapp_num
