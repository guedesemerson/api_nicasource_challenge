from rest_framework.generics import GenericAPIView, ListAPIView
from .serializers import RatingSerializer, ViewRatingSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rating.models import Rating


class RegisterRatingView(GenericAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RatingSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListRatingView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = ViewRatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['movie']