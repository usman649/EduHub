from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return  request.user.is_authenticated and request.user.role == 1

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return  request.user.is_authenticated and  request.user.role == 2