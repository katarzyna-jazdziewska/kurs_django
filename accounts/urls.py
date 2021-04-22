from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
# from django.contrib.auth.views import LoginView
from accounts.views import (
    SubmittableLoginView, SubmittablePasswordChangeView,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password_change')
]
