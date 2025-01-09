from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        return False

