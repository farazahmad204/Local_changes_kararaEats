from django import forms

from .models import Mail

class ContactUsForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100 ,widget=forms.TextInput(attrs={'placeholder': 'Your name', 'size': '50','maxlength': '100','class': 'no-border'}))
    email   = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'placeholder': 'Your Email', 'size': '50','class': 'no-border'}))
    mobile  = forms.IntegerField(label='Mobile',widget=forms.TextInput(attrs={'placeholder': 'Mobile or Phone' , 'size': '50','class': 'no-border '}))
    message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'placeholder': 'Type your message here' , 'rows': '5' ,'class': 'no-border custom-textarea'}))
    # Add more fields as needed


    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Mail.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.Please change")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Mail.objects.filter(name= username).exists():
            raise forms.ValidationError("This username is already in use.Please change")
        return username
    
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if Mail.objects.filter(mobile= mobile).exists():
            raise forms.ValidationError("This Mobile No is already in use.Please change")
        return mobile