# from django.contrib import auth
# from django.contrib.auth import load_backend
# from django.contrib.auth.backends import RemoteUserBackend
import logging
from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import MiddlewareMixin
from poc.backends import RemoteUserCustomBackend
from rest_framework.exceptions import AuthenticationFailed
from poc.thread_local import request_data


class RemoteUserMiddleware(MiddlewareMixin):
    """
    Middleware for utilizing web-server-provided authentication.

    If request.user is not authenticated, then this middleware attempts to
    authenticate the username passed in the ``HTTP_AUTHORIZATION`` request header.
    If authentication is successful, the user is automatically logged in to
    persist the user in the session.

    The header used is configurable and defaults to ``HTTP_AUTHORIZATION``.  Subclass
    this class and change the ``header`` attribute if you need to use a
    different header.
    """

    # Name of request header to grab username from.  This will be the key as
    # used in the request.META dictionary, i.e. the normalization of headers to
    # all uppercase and the addition of "HTTP_" prefix apply.
    header = "HTTP_AUTHORIZATION"
    force_logout_if_no_header = True
   
    def process_request(self, request):
        # AuthenticationMiddleware is required so that request.user exists.                
        auth = RemoteUserCustomBackend() 
        try:
            user = auth.authenticate(request)
            if user:        
                request.user, token = user
                request_data.user = request.user
        except AuthenticationFailed:
            logging.warning('Invalid token')