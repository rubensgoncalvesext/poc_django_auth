import json
import requests


url_api = "https://gestao-dev.dgranel.com.br/api/auth/token/"

payload = json.dumps({
    "username": "105.544.806-38",
    "password": "105@Dgranel"
})

headers = {
    'Content-Type': 'application/json',
}

response = requests.request("POST", url_api, headers=headers, data=payload)
token = response.json()["token"]

URL = "http://localhost:8000/product/"

HEADER = {'Authorization': f'Bearer {token}'}

res = requests.get(URL, headers=HEADER)
