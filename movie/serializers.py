from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'release_date',
            'genre',
            'plot',
        )
        read_only_fields = [
            'id'
        ]


class DetailMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'release_date',
            'genre',
            'plot',
        )




