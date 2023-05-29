import pytest
from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


def test_rating_post(admin_client, movie, user):
    user_object = {
        "user": user.id,
        "score": 9.5,
        "comment": "test_pass",
        "movie": movie.id,
    }
    url = reverse('api-rating:register_rating')
    response = admin_client.post(url, data=user_object)
    print(response.json)
    assert response.status_code == status.HTTP_201_CREATED


def test_rating_list(admin_client):
    url = reverse('api-rating:list_rating')
    response = admin_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK
