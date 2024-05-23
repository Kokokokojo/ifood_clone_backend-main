from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from twilio.rest import Client
import os


def send_mail(email:str, type:str):

    email_html_message = render_to_string('email/takeaway.html', {
        "email":email, 
    })
    email_plaintext_message = render_to_string('email/takeaway.txt', {
        "email":email, 
    })
    
    if type == 'cancelled':

        email_html_message = render_to_string('email/cancelled.html', {
            "email":email, 
        })
        email_plaintext_message = render_to_string('email/cancelled.txt', {
            "email":email, 
        })

    msg = EmailMultiAlternatives(
            # title:
            f"Atualização do seu pedido! - Bytefood",
            # message:
            email_plaintext_message,
            # from:
            settings.EMAIL_HOST_USER,
            # to:
            [email]
        )

    msg.attach_alternative(email_html_message, "text/html")
                           
    msg.send()



def send_sms(phone_number:str, message:str):
    account_sid = os.environ.get('account_sid')
    auth_token =  os.environ.get('auth_token')
    twilio_phone_number =  os.environ.get('twilio_phone_number')

    client = Client(account_sid, auth_token)

    client.messages.create(
        body = f'{message}',
        from_ = twilio_phone_number,
        to = phone_number
    )