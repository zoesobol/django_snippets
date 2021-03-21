from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(subject, body, recipient):
    send_mail(subject,
    body,
    'zoecuentarandom@gmail.com',
    [recipient])

