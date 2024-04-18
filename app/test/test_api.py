import json
import requests
from django.test import TestCase
from product.models import Product
from rest_framework import status
from poc import settings
from remote_users.models import AuthtokenToken

url_api = settings.EXTERNAL_URL

class ProductTestCase(TestCase):
    databases = {"default", "external_db"}
    URL = "/product/"
    
    def get_token(self):
        
        payload = json.dumps({
            "username": settings.USERNAME,
            "password": settings.PASSWORD
        })

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url_api, headers=headers, data=payload)
        response.json()["token"]
    
    def get_local_token(self):
        return AuthtokenToken.objects.first().key
 
    def setUp(self):
        self.product = Product.objects.create(name='test', price=10)

    def test_remote_auth_remote_invalid_token(self):
        token = self.get_token()

        response = self.client.get(
            self.URL,
            data={},
            format="json",
            **{"HTTP_AUTHORIZATION": f"Bearer {token}"},
            follow=True,
        )
        data_response = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # self.assertEqual(len(data_response), 1, "Total register is equal 1")


    def test_remote_auth_not_successfully(self):
        response = self.client.get(
            self.URL,
            data={},
            format="json",
            follow=True,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_remote_auth_get_local_token_path_successfully(self):
        token = self.get_local_token()

        response = self.client.get(
            self.URL,
            data={},
            format="json",
            **{"HTTP_AUTHORIZATION": f"Bearer {token}"},
            follow=True,
        )
        data_response = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(data_response), 1, "Total register is equal 1")

        
class LoginTestCase(TestCase):
    URL = "/login/"

    def test_login_auth_success_path(self):
        response = self.client.post(
                self.URL,
                data={},
                **{"REMOTE_USER": f"fake_user"},
                follow=True,
            )

        print(response.content)

        self.assertEqual(str(response.content), "b'Hello, fake_user!'", "User not logged")
        # Assuming your Django app is served at http://localhost:8000/

        # <Location "/">
        #     AuthType Basic
        #     AuthName "Your Site"
        #     Require valid-user
        #     SetEnvIf Request_URI "^/" HTTP_REMOTE_USER=%{REMOTE_USER}
        #     RequestHeader set REMOTE_USER %{HTTP_REMOTE_USER}e
        # </Location>

class LoginAuthTestCase(TestCase):
    URL = "/login/"

    def test_login_auth_success_path(self):
        response = self.client.post(
                self.URL,
                data={},
                **{"HTTP_AUTHORIZATION": f"Bearer fake_token"},
                follow=True,
            )

        print(response.content)

        self.assertEqual(str(response.content), "b'Hello, fake_user!'", "User not logged")