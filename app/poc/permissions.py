from django.contrib.auth.models import Permission
from remote_users.models import UsersUser
from rest_framework.permissions import BasePermission
from django.contrib.auth.backends import RemoteUserBackend

class IsAuthenticated(BasePermission): # trocar o BasePermission
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
    
    def token_validation(self, auth_info):
        # request no servidor antigo e validar o token ????
        # nao multiples request devolvendo para o server antigo, agente poderia implement cached.
        # timetolive ≃ 365 dias.
        # pendente a criacao do method validate_token ???
        user_id = 1

        user = UsersUser.objects.filter(pk=user_id)
        return True