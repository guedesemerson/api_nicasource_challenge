from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = (
            'id',
            'user',
            'score',
            'comment',
            'movie',
        )
        read_only_fields = [
            'id'
        ]

    def validate(self, attrs):
        user = attrs.get('user', '')
        movie = attrs.get('movie', '')
        if Rating.objects.filter(user=user, movie=movie ).exists():
            raise serializers.ValidationError(
                {'response': f'User: {user.username} already rated this movie'}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)


class ViewRatingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='email'
    )

    class Meta:
        model = Rating
        fields = (
            'user',
            'score',
            'comment',
            'movie',
        )

