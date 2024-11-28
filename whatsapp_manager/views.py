from django.shortcuts import render, redirect
from .forms import WhatsAppMessageForm
from accounts.models import CustomUser  # Adjust the import based on your app structure
import requests

def send_whatsapp_template_message(phone_number,message):
    phone_number = "923124949579"
    ACCESS_TOKEN = "EAAP1PR8e7E8BO04bHvHKnKZCAEWZAY7rDUWN03oT1MiiUPNuLhtveiZBZBUUQMvI3uG4SbGQ9ACKnWqUkDRYbhZBuXBb3I5OyLsH0cw5U6qxZA7l1gWCVcy9wPjIS5hcenAXIJzkaQKY5uhvJFHlu43La8w9ZArzyXdjFceZCZCeFRcsBHfMTP4ZC8j6m2zhSTZAVk05dI9CGYlNs45KBR391pRbGq5OuJmHZCtOsZAh2pCLciswHqZCWWGZAoJ"
    PHONE_NUMBER_ID = "391767824029459"

    url = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message
        }
    }

    try:
        print(url)
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raises an error for 4xx or 5xx responses
        print(f"Message sent successfully to {phone_number}: {response.json()}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to {phone_number}: {e}")
        return False

def whatsapp_message_view(request):
    users = CustomUser.objects.all()

    if request.method == 'POST':
        form = WhatsAppMessageForm(request.POST)
        selected_users = request.POST.getlist('selected_users')

        if form.is_valid() and selected_users:
            message_template = form.cleaned_data['message_template']
            sent_successfully = []
            failed_to_send = []

            for user_id in selected_users:
                user = CustomUser.objects.get(id=user_id)
                if send_whatsapp_template_message(user.whatsapp_num, message_template):
                    sent_successfully.append(user)
                else:
                    failed_to_send.append(user)

            # Render the result page with lists of successes and failures
            return render(request, 'whatsapp_manager/send_result.html', {
                'sent_successfully': sent_successfully,
                'failed_to_send': failed_to_send,
            })
    else:
        form = WhatsAppMessageForm()

    return render(request, 'whatsapp_manager/send_message.html', {
        'form': form,
        'users': users,
    })
