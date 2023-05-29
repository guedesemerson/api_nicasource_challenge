from datetime import timedelta
from django.utils import timezone
from oauth2_provider.models import AccessToken, Application
from rest_framework.test import APIClient
from user.models import User
from movie.models import Movie
import pytest


@pytest.fixture
def admin_client(admin_user, application_client):
    access_token = AccessToken.objects.create(
        user=admin_user,
        scope="read write",
        expires=timezone.now() + timedelta(seconds=300),
        token="secret-access-token-key",
        application=application_client
    )

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token.token)
    client.force_authenticate(user=admin_user)

    return client


@pytest.fixture
def application_client(admin_user):
    return Application.objects.create(
        name="Test Application",
        redirect_uris="http://localhost http://example.com http://example.org",
        user=admin_user,
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
    )


@pytest.fixture
def user():
    user = User()
    user.email = "user@example.com"
    user.password = "test_pass"
    user.save()
    return user


@pytest.fixture
def movie():
    movie = Movie()
    movie.title = 'movie1'
    movie.release_date = '2023-05-27'
    movie.genre = 'Horror'
    movie.plot = 'my plot'
    movie.save()
    return movie