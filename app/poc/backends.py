# from django.contrib.auth.backends import BaseBackend, RemoteUserBackend, ModelBackend
from rest_framework.authentication import TokenAuthentication
from remote_users.models import AuthtokenToken

class RemoteUserCustomBackend(TokenAuthentication):
    model = AuthtokenToken
    keyword = 'Bearer'
   