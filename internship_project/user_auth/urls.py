from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path(
        "forgot-password/",
        views.CustomPasswordResetView.as_view(),
        name="forgot_password",
    ),
    path("change-password/", views.change_password_view, name="change_password"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
