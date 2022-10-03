from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),  # Home route for dashboard after logging in
    path("profile/<int:pk>", views.UserDetailView.as_view(), name='profile.view'),  # Endpoint to view user profile based on pk
    path("profile/<int:pk>/edit", views.UserUpdateView.as_view(), name='profile.edit'),  # Endpoint to edit a profile
    path("all-profiles", views.ProfileListView.as_view(), name='profile.list'),  # Endpoint to display all user profiles
    path("new", views.UserCreateView.as_view(), name='profile.new'),  # Endpoint to create new user profiles
]
