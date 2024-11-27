from django import forms

class WhatsAppMessageForm(forms.Form):
    message_template = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your message template here...'}),
        label='Message Template'
    )
