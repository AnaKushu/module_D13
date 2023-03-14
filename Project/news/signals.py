from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from .tasks import send_notify


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers_emails = []
        for postCategory in categories:
            subscribers = postCategory.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notify.delay(instance.preview(), instance.pk, instance.title, subscribers_emails)
