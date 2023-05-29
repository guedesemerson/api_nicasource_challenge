from rest_framework.generics import (ListAPIView,
                                     GenericAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
from .serializers import MovieSerializer, DetailMovieSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Movie


class RegisterMovieView(GenericAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = MovieSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMovieView(ListAPIView):

    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all().order_by('release_date')


class RetrieveMovieView(RetrieveAPIView):

    serializer_class = DetailMovieSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Movie.objects.filter(id=self.kwargs['id'])


class DeleteMovieView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        queryset = Movie.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        instance.delete()


class UpdateMovieView(UpdateAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Movie.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()