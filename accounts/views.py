from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy


class SubmittableLoginView(LoginView):
    template_name = 'accounts/login.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')

