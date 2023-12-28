from django.db.models.signals import post_save
from django.dispatch import receiver
from Blog.tasks import send_mail_celery
from .models import PostModel, Subscription


@receiver(post_save, sender=PostModel)
def send_email_on_post_save(sender, instance, created, **kwargs):
    if created:
        result = Subscription.objects.filter(author_sub=instance.post_author)
        for i in result:
            email_send = str(i.user_sub)
            author_send = str(instance.post_author)
            send_mail_celery.delay(email_send, author_send)
