from django.contrib.auth.backends import BaseBackend, RemoteUserBackend, ModelBackend


class RemoteUserCustomBackend(ModelBackend):
    print('entrei auth')
    def authenticate(self, request, token=None):
        print("entrei authenticate")
        print(request.META['HTTP_AUTHORIZATION'])

        # validation_token() -> backend_sistema_velho

        #if validation_token:
            # user = UsersUser.objects.filter(pk=user_id)
            # print(user)
            # return user
