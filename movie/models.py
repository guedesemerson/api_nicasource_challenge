from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    release_date = models.DateField(verbose_name='Release Date')
    genre = models.CharField(max_length=100, verbose_name='Genre')
    plot = models.TextField(verbose_name='Plot')

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title
