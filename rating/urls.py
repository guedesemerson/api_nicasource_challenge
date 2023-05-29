from django.urls import path
from .views import RegisterRatingView, ListRatingView

app_name = "api-rating"

urlpatterns = [
    path('register_rating', RegisterRatingView.as_view(), name='register_rating'),
    path('list_rating', ListRatingView.as_view(), name='list_rating'),
]