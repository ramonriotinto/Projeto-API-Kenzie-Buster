from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser


class UserEmployeePermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        if request.user.is_employee is True:
            return True
        elif request.user == user:
            return True
        elif request.user.is_employee is False and request.user != user:
            return False
