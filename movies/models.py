from django.db import models
from users.models import User


class Indications(models.TextChoices):
    DEFAULT = "G"
    RATED_PG = "PG"
    RATED_PG_13 = "PG-13"
    RATED_R = "R"
    RATED_NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(
        max_length=20,
        choices=Indications.choices,
        default=Indications.DEFAULT,
    )
    synopsis = models.TextField(null=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
    )

    order = models.ManyToManyField(
        User,
        through="movies.MovieOrder",
        related_name="movie_orders",
    )


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movies_order",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movies_order",
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
