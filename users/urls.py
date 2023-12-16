from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_new_password, activate

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('register/verify_email/', TemplateView.as_view(template_name='users/verify.html'), name='verify_email'),
    path('register/success/', TemplateView.as_view(template_name='users/success_verify.html'), name='success_verify'),
    path('register/failure/', TemplateView.as_view(template_name='users/failure_verify.html'), name='failure_verify'),
    path('activate/<uidb64>[0-9A-Za-z]+<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}', activate, name='activate'),
]
