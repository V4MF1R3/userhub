from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import CustomUserCreationForm


def home_view(request):
    """Redirect to the login page."""
    return redirect("login")


def login_view(request):
    """Handle user login."""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def signup_view(request):
    """Handle user signup."""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account created successfully! You can now log in."
            )
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})


class CustomPasswordResetView(PasswordResetView):
    """Custom Password Reset View."""

    template_name = "forgot_password.html"
    success_url = reverse_lazy("login")
    email_template_name = "password_reset_email.html"
    form_class = PasswordResetForm


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """Custom Password Reset Confirm View."""

    template_name = "password_reset_confirm.html"
    success_url = reverse_lazy("login")
    form_class = SetPasswordForm


@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Keep the user logged in
            messages.success(request, "Your password was successfully updated!")
            return redirect("dashboard")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form": form})


@login_required
def dashboard_view(request):
    """Render the dashboard page for logged-in users."""
    return render(request, "dashboard.html", {"username": request.user.username})


@login_required
def profile_view(request):
    """Render the profile page for the logged-in user."""
    user = request.user
    return render(
        request,
        "profile.html",
        {
            "username": user.username,
            "email": user.email,
            "date_joined": user.date_joined,
            "last_login": user.last_login,
        },
    )


def logout_view(request):
    """Handle user logout."""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect("login")
