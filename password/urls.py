from django.urls import path
from .views import (
    PasswordCreateView,
    PasswordListView,
    PasswordDetailView,
    PasswordUpdateView,
    PasswordDeleteView,
    login_user,
    logout_user,
)


urlpatterns = [
    path(
        "",
        PasswordListView.as_view(),
        name="password_list",
    ),
    path(
        "<int:pk>/detail/",
        PasswordDetailView.as_view(),
        name="password_detail",
    ),
    path(
        "add/",
        PasswordCreateView.as_view(),
        name="password_create",
    ),
    path(
        "<int:pk>/",
        PasswordUpdateView.as_view(),
        name="password_update",
    ),
    path(
        "<int:pk>/delete/",
        PasswordDeleteView.as_view(),
        name="password_delete",
    ),
    path(
        "login/",
        login_user,
        name="login",
    ),
    path(
        "logout/",
        logout_user,
        name="logout",
    ),
]
