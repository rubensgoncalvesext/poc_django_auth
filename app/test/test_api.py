import json
import requests
from django.test import TestCase
from product.models import Product
from rest_framework import status

url_api = "https://gestao-dev.dgranel.com.br/api/auth/token/"

class ProductTestCase(TestCase):
    URL = "/product/"
    
    def get_token(self):
        
        payload = json.dumps({
            "username": "105.544.806-38",
            "password": "105@Dgranel"
        })

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url_api, headers=headers, data=payload)
        return response.json()["token"]

    def setUp(self):
        self.product = Product.objects.create(name='test', price=10)

    def test_remote_auth_path_successfully(self):
        token = self.get_token()

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