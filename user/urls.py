from django.urls import path
from .views import RegisterUserView, AuthenticateUserView


app_name = "api-user"

urlpatterns = [
    path('register_user', RegisterUserView.as_view(), name='register_user'),
    path('authenticate_user', AuthenticateUserView.as_view(), name='authenticate_user'),
]