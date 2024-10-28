from django import forms
from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'picture', 'price', 'quantity', 'description']  # Fields that will be shown in the form

    # Adding widgets to customize the form appearance
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),
        label='Item Name'
    )
    picture = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label='Item Picture'
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        label='Price'
    )
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        label='Quantity'
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        label='Description',
        required=False
    )
