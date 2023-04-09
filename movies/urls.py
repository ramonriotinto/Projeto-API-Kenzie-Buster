from django.urls import path
from .views import MoviesView, MoviesDetailView, MoviesOrderDetailView

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", MoviesDetailView.as_view()),
    path("movies/<int:movie_id>/orders/", MoviesOrderDetailView.as_view()),
]
