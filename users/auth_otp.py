import random 
import string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from twilio.rest import Client
import os

# Generate a one time password
def generate_otp(length=6):
    chars = string.digits
    otp = ''.join(random.choice(chars) for _ in range(length))
    return otp


# Send one time password via email
def send_otp_email(email, otp, user_full_name):

    email_html_message = render_to_string('email/otp_email.html', {
        "email":email, 
        "otp":otp,
        "user_name":user_full_name or 'User'
    })
    email_plaintext_message = render_to_string('email/otp_text.txt', {
        "email":email, 
        "otp":otp,
        "user_name":user_full_name or 'User'

    })


    msg = EmailMultiAlternatives(
            # title:
            "Your One time password is here! - {title}".format(title="Bytefood"),
            # message:
            email_plaintext_message,
            # from:
            settings.EMAIL_HOST_USER,
            # to:
            [email]
        )

    msg.attach_alternative(email_html_message, "text/html")
                           
    msg.send()


# Send one time password via phone

def send_otp_phone(phone_number, otp, user_full_name):
    account_sid = os.environ.get('account_sid')
    auth_token =  os.environ.get('auth_token')
    twilio_phone_number =  os.environ.get('twilio_phone_number')


    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = f'Your one time password: {otp}',
        from_ = twilio_phone_number,
        to = phone_number
    )