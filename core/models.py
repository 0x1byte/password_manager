from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(
        upload_to="profiles/",
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save()

        if self.profile_image:
            img = Image.open(self.profile_image.path)

            if img.height > 100 or img.width > 100:
                new_img = (100, 100)
                img.thumbnail(new_img)
                img.save(self.profile_image.path)
