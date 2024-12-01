import time
from datetime import datetime

from django.shortcuts import render, redirect
from .forms import WhatsAppMessageForm
from accounts.models import CustomUser  # Adjust the import based on your app structure
from order.models import Order
import requests
import threading
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


from django.db.models import Prefetch


def customers_without_orders(start_date, end_date):
    """
    Fetch all orders with the user's WhatsApp number.

    Returns:
        list: A list of dictionaries containing order details and the WhatsApp number of the user.
    """

    # Prefetch related user information for efficiency
    orders = Order.objects.filter(
    created_at__range=(start_date, end_date)  # Filter orders within the date range
        ).select_related('user').values(
        'user__whatsapp_num',  # WhatsApp number of the user
        'user__username',  # Username of the user
    )
    all_customers = CustomUser.objects.values_list('whatsapp_num', flat=True)
    whatsapp_num = []
    for order in orders:
        whatsapp_num.append(order['user__whatsapp_num'])
    result = [pnum for pnum in all_customers if pnum not in whatsapp_num]

    return result


def order_reminder_task(message):
    # get latest date and time
    start_date = datetime.now()

    print("waiting for 1 week...")
    time.sleep(604800)
    end_date = datetime.now()
    whats_app_nums=customers_without_orders(start_date, end_date)
    for number in whats_app_nums:
        send_whatsapp_template_message(number, message)

def menu_uploading_reminder(message):
    all_customers = CustomUser.objects.values_list('whatsapp_num', flat=True)
    for number in all_customers:
        send_whatsapp_template_message(number, message)

def whatsapp_message_initiates(**kwargs):
    message = kwargs.get('message',"")
    message_type = kwargs.get('message_type',"menu_reminder")
    threads = []
    if message_type == 'menu_reminder':
        threads.append(threading.Thread(target=menu_uploading_reminder, args=(message,)))
    if message_type == 'order_reminder':
        threads.append(threading.Thread(target=menu_uploading_reminder, args=(message,)))
    for thread in threads:
        thread.start()