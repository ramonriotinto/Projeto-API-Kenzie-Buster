from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from users.permissions import CustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class MoviesView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomPermission]

    def get(self, request):
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies, request, view=self)

        movies_serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(movies_serializer.data)

    def post(self, request):
        movie_serializer = MovieSerializer(data=request.data)
        movie_serializer.is_valid(raise_exception=True)
        movie_serializer.save(user=request.user)

        return Response(movie_serializer.data, status.HTTP_201_CREATED)


class MoviesDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomPermission]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie_serializer = MovieSerializer(movie)

        return Response(movie_serializer.data, status.HTTP_200_OK)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesOrderDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        movie_serializer = MovieOrderSerializer(data=request.data)
        movie_serializer.is_valid(raise_exception=True)
        movie_serializer.save(user=request.user, movie=movie)

        return Response(movie_serializer.data, status.HTTP_201_CREATED)
