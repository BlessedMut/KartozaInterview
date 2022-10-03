from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import CreateView


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """
        This function checks if a user is logged in before they are registered,
        It checks if a user is not already authenticated before they register
        :param request:
        :param args:
        :param kwargs:
        :return: redirect to home route if already logged in
        """
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)


# Login endpoint
class LoginInterfaceView(LoginView):
    template_name = 'users/login.html'


# Logout endpoint
class LogoutInterfaceView(LogoutView):
    template_name = 'users/logout.html'
