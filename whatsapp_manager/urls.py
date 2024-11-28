from django.urls import path
from .views import whatsapp_message_view

urlpatterns = [
    path('send-message/', whatsapp_message_view, name='send_message'),
    #path('send-message/', whatsapp_message_view, name='send_message'),
]
