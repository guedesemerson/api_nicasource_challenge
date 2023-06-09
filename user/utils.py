import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None

        my_auth = list(auth_data.decode('utf-8').split(' '))

        if len(my_auth) > 1:
            my_auth.remove('Bearer')

        token = my_auth[0]

        try:
            payload = jwt.decode(token, str(settings.JWT_SECRET_KEY))
            user = User.objects.get(username=payload['username'])
            return user, token

        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed(
                'Token invalid!')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'Token expired!')

        return super().authenticate(request)