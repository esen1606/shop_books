from django.core.mail import send_mail
from django.utils.html import format_html
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from twilio.rest import Client
from django.conf import settings


account_sid = settings.TWILIO_SID
auth_token = settings.TWILIO_AUTH_TOKEN
twilio_sender = settings.TWILIO_SENDER_PHONE

# def send_confirmation_email(email, code):
#     send_mail(
#         'Здравствуйте активируйте ваш аккаунт!',
#         f'Чтобы ваш аккаунт скопируйте и введите на сайте код: {code}',
#         'antonchzhu@gmail.com',
#         [email],
#         fail_silently=False,
#     )

def send_confirmation_email(email , code):
    activation_url = f'http://127.0.0.1:8000/api/account/activate/?u={code}'
    context = {'activation_url': activation_url}
    subject = 'Здраствуйте потвердите свое присудствие '
    html_message = render_to_string('activate.html',context)
    plain_message = strip_tags(html_message)
    
    
    send_mail(
        subject,
        plain_message,
        'esenkackynbaev6@gmail.com',
        [email],
        html_message=html_message,
        fail_silently=False
    )

def send_activation_sms(phone_number, activation_code):
    message = f'Ваш код активации: {activation_code}'
    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_=twilio_sender, to=phone_number)
    
def send_confirmation_password(email, code):
    activation_url = f'http://127.0.0.1:8000/api/account/reset_password/confirm/?u={code}'
    context = {'activation_url': activation_url}
    subject = 'Подтвердите изменение пароля'
    html_message = render_to_string('account/new_password.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        'admin@gmail.com',
        [email],
        html_message=html_message,
        fail_silently=True
    )