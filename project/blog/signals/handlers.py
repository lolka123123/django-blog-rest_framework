from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from blog import models

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, **kwargs):
    if kwargs['created']:
        models.Profile.objects.create(user=kwargs['instance'])