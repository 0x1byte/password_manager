from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import User
from os.path import isfile
from os import remove


@receiver(post_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    if isfile(instance.profile_image.path):
        remove(instance.profile_image.path)


@receiver(pre_save, sender=User)
def update_profile(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        user = User.objects.get(pk=instance.pk)
    except User.DoesNotExist:
        return False
    if not user.profile_image == instance.profile_image and user.profile_image:
        if isfile(user.profile_image.path):
            remove(user.profile_image.path)
