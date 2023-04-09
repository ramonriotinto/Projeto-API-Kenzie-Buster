from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer, CustomJwtSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import UserEmployeePermission


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJwtSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserGetDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, UserEmployeePermission]

    def get(self, request, user_id: int):
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status.HTTP_200_OK)

    def patch(self, request, user_id: int):
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        user_serializer = UserSerializer(user, request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response(user_serializer.data, status.HTTP_200_OK)
