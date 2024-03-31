from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import User


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "core/profile_update.html"
    fields = ["username", "first_name", "last_name", "email", "profile_image"]
    success_url = "/"

    def get_object(self, queryset=None):
        return User.objects.get(username=self.request.user)
