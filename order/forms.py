from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']  # Fields that will be shown in the form

    # Adding widgets to customize the form appearance
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=Order.ORDER_STATUS_CHOICES,
        label='Order Status'
    )
