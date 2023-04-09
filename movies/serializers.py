from rest_framework import serializers
from .models import Indications, Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(
        choices=Indications.choices,
        default=Indications.DEFAULT,
    )
    synopsis = serializers.CharField(default=None)
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source="movie.title", read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.CharField(source="user.email", read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
