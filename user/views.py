from rest_framework.generics import GenericAPIView
from .serializers import UserSignupSerializer, UserAuthenticateSerializer

from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import authenticate
from .models import User
import jwt


class RegisterUserView(GenericAPIView):
    serializer_class = UserSignupSerializer

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthenticateUserView(GenericAPIView):
    serializer_class = UserAuthenticateSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')

        try:
            object_pass = User.objects.get(email=email)

        except:
            return Response('Invalid credentials', status=status.HTTP_400_BAD_REQUEST)
        username = object_pass.username
        user = authenticate(username=username, password=password)
        if not user:
            user = User.objects.filter(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': username}, str(settings.JWT_SECRET_KEY))

            data = {'email': email, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



