from django.contrib import admin
from .models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = [
        "website",
        "username",
        "phone",
        "password",
        "created_at",
        "updated_at",
    ]
    list_filter = ["website", "username", "phone"]
    search_fields = [
        "website",
        "username",
        "password",
    ]
    ordering = ["-created_at"]
