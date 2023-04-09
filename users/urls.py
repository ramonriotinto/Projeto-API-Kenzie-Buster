from django.urls import path
from .views import UserView, LoginJWTView, UserGetDetailView
from rest_framework_simplejwt import views

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserGetDetailView.as_view()),
    path("users/login/", LoginJWTView.as_view()),
    path("users/login/refresh/", views.TokenRefreshView.as_view()),
]
