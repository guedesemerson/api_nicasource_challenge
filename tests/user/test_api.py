import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_user_api_register(admin_client):
    user_object = {
        "email": "user@example.com",
        "username": "test",
        "password": "test_pass",
    }
    url = reverse('api-user:register_user')
    response = admin_client.post(url, data=user_object)

    assert response.status_code == status.HTTP_201_CREATED


def test_user_api_authenticate(admin_client, user):
    user_object = {
        "email": user.email,
        "password": user.password
    }

    url = reverse('api-user:authenticate_user')
    response = admin_client.post(url, data=user_object)
    assert response.status_code == status.HTTP_200_OK


