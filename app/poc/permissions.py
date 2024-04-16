from django.contrib.auth.models import Permission
from rest_framework.permissions import BasePermission
from django.contrib.auth.backends import RemoteUserBackend

class Permission(BasePermission):
    def has_permission(self, request, view):
        header = request.environ.get("HTTP_AUTHORIZATION")
        if not header:
            return False
        try:
            auth_type, auth_info = header.split(None, 1)
            auth_type = auth_type.lower()
        except ValueError:
            return False

        if auth_info is None or not auth_info:
            return False
        return self.token_validation(auth_info)
    
    def token_validation(self, request, *args, **kwargs):
        return True