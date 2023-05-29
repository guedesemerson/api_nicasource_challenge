from django.urls import path
from .views import (RegisterMovieView,
                    ListMovieView,
                    RetrieveMovieView,
                    DeleteMovieView,
                    UpdateMovieView,
                    )

app_name = "api-movie"

urlpatterns = [
    path('register_movie', RegisterMovieView.as_view(), name='register_movie'),
    path('list_movie', ListMovieView.as_view(), name='list_movie'),
    path('retrieve_movie/<int:id>', RetrieveMovieView.as_view(), name='retrieve_movie'),
    path('delete_movie/<int:id>', DeleteMovieView.as_view(), name='delete_movie'),
    path('update_movie/<int:id>', UpdateMovieView.as_view(), name='update_movie')
]