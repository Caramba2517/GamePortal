from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from ads.models import Reply


@receiver(post_save, sender=Reply)
def reply_send_mail(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='New reply!',
            message=f'{instance.author} responded to your ad {instance.ad}.'
                    f'Look more? http://127.0.0.1:8000/accounts/profile/',
            recipient_list=[instance.ad.author.email],
            from_email='caramba.ge@yandex.ru'
        )
    else:
        send_mail(
            subject='Aproved!',
            message=f'{instance.ad.author} aproved your reply {instance.comment}',
            recipient_list=[instance.author.email],
            from_email='caramba.ge@yandex.ru'
        )





