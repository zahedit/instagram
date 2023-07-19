from django.urls import path
from user.views import RegisterView, LoginView

urlpatterns = [
    path('register', RegisterView.as_view(), name='auth-register'),
    path('login', LoginView.as_view(), name='auth-login'),
]
