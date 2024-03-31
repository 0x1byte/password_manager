from django.shortcuts import redirect, render
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from .models import Password


class PasswordListView(LoginRequiredMixin, ListView):
    template_name = "password/password_list.html"
    model = Password

    def get_queryset(self):
        return Password.objects.filter(user=self.request.user)


class PasswordDetailView(LoginRequiredMixin, DetailView):
    template_name = "password/password_detail.html"
    model = Password

    def get_queryset(self):
        return Password.objects.filter(user=self.request.user)


class PasswordCreateView(LoginRequiredMixin, CreateView):
    template_name = "password/password_create.html"
    model = Password
    success_url = "/"
    fields = ["website", "username", "phone", "password"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PasswordUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "password/password_update.html"
    model = Password
    success_url = "/"
    fields = ["website", "username", "phone", "password"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PasswordDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "password/password_delete.html"
    model = Password
    success_url = "/"


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/login/")
