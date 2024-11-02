from django.shortcuts import redirect, render

from .models import Mail

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import EmailMultiAlternatives

from django.core.mail import send_mail

from django.contrib import messages

from order.models import FoodItem, Menu, Order, OrderItem



from .forms import ContactUsForm




DEFAULT_FROM_EMAIL = 'farazahmed204@gmail.com'

username= None




# Create your views here.
def send_emails(request,user_email='None'):
    emails = Mail.objects.values_list('email', flat=True)  # Assuming YourModel has an 'email' field
    subject = 'This is a Sample Subject'
    message = 'This is a sample Content Your email content here'

    for email in emails:
        if email == user_email:
            all_values= Mail.objects.filter(email=user_email).values()#Mail.objects.all().values()
            message_html= render_to_string('email/email.html',{
            'all_values':all_values,
            'subject': subject,
            'message':message,
            'name':username
            })

            send_mail(subject, message, 'farazahmed204@gmail.com', [email], html_message=message_html)

    return None


def contact_us(request):
    global username

    if request.method == 'POST':
        #object for Form and also checks each field if it is present in existing data base 
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Process form data
             try:
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                mobile = form.cleaned_data['mobile']
                message=form.cleaned_data['message']

                #Create an instance of Mail (save it into DB in Mail Table)
                mail_instance = Mail(
                name = username,
                email = email,
                slug= username,
                mobile= mobile,
                message= message            
                 )
                # Save the instance to the database
                mail_instance.save()

                # Optionally, show success message
                message='Hello '+ username +'\n Your query is received successfully!!! our team will contact with you shortly' 
                messages.success(request, message)

                send_emails(request,email)
                return redirect('contact_us')  # Redirect to a success page   
    
             except Exception as e:
                 message='Hello '+ username +'\n There is a problem with our database ' 
                 messages.error(request, message)
    else:
        form = ContactUsForm()

    return render(request,'contact_us.html', {'form': form})

def send_order_confirmation_email(request,user_email='None', context=None ):

    emails = Mail.objects.values_list('email', flat=True)  # Assuming YourModel has an 'email' field
    subject = 'Order Confirmation'
    message = 'This is a sample Content Your email content here'

    for email in emails:
        if email == user_email:
            all_values= Mail.objects.filter(email=user_email).values()#Mail.objects.all().values()
            message_html= render_to_string('email/order_confirmation.html',context=context)
            send_mail(subject, message, 'farazahmed204@gmail.com', [email], html_message=message_html)

    return None
