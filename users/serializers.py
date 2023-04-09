from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJwtSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_employee"] = user.is_employee

        return token


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(User.objects.all(), message="username already taken.")
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(User.objects.all(), message="email already registered.")
        ]
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict):
        if validated_data["is_employee"] is True:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        pop_password = validated_data.pop("password")

        if pop_password:
            instance.set_password(pop_password)
            instance.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
