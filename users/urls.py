from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.SignupView.as_view(), name="register"),  # New user registration endpoint
    path("logout/", views.LogoutInterfaceView.as_view(), name="logout"),  # Logout endpoint
    path("login/", views.LoginInterfaceView.as_view(), name="login"),  # Login endpoint
]
