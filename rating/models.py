from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from user.models import User
from movie.models import Movie


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Rating User")
    score = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name='Score',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    comment = models.TextField(verbose_name='Comment')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Movie')

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return str(self.score)
