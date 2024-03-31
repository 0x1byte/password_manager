from django.db import models
from django.conf import settings


class Password(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="passwords",
    )
    website = models.CharField(max_length=255)
    username = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
    )
    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
    )
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website

    class Meta:
        ordering = ["-created_at"]
