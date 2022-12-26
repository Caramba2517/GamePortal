from celery import shared_task
from django.core.mail import send_mail
from ads.models import Ads, User
from datetime import datetime, timedelta


@shared_task
def week_email():
    mail_list = [mail.email for mail in User.objects.all() if mail.email]
    message = ''
    for ad in Ads.objects.filter(time_create__gt=datetime.now() - timedelta(days=7)):
        message += f'{ad.tittle}\n'
        send_mail(
            subject=f'Ads per week',
            message=message,
            from_email='caramba.ge@yandex.ru',
            recipient_list=mail_list
        )