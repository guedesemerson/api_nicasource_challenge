import pytest
from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


def test_movie_list(admin_client):
    url = reverse('api-movie:list_movie')
    response = admin_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK


def test_movie_api_detail(admin_client, movie):
    url = reverse('api-movie:retrieve_movie', args=[movie.id])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['id'] == movie.id


def test_movie_api_update(admin_client, movie):
    url = reverse('api-movie:update_movie', args=[movie.id])
    response = admin_client.patch(url, data={'title': 'new_title'})
    assert response.status_code == status.HTTP_200_OK


def test_movie_api_delete(admin_client, movie):
    url = reverse('api-movie:delete_movie', args=[movie.id])
    response = admin_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT