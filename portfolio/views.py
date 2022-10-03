# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView

from portfolio.forms import UserForm
from portfolio.models import Profiles


# Home based view to render a home template with a map and markers for logged in user
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "portfolio/home.html"
    extra_context = {}
    login_url = '/users/login'


# Create new user endpoint
class UserCreateView(CreateView):
    model = Profiles
    form_class = UserForm
    success_url = '/'
    template_name = 'portfolio/user.html'


# Endpoint to update user
class UserUpdateView(UpdateView):
    model = Profiles
    form_class = UserForm
    success_url = '/all-profiles'
    template_name = 'portfolio/user.html'


# Endpoint to view all user Details
class UserDetailView(DetailView):
    model = Profiles
    context_object_name = "profiles"
    success_url = 'all-profiles'
    template_name = 'portfolio/profile_detail.html'


# Endpoint to display all profiles
class ProfileListView(ListView):
    model = Profiles
    context_object_name = "profile"
    template_name = "portfolio/profile_list.html"
