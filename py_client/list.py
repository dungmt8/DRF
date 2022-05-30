import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'
password = getpass()
data = {
    'username': 'admin',
    'password': password
}

auth_response = requests.post(auth_endpoint, json=data)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = 'http://localhost:8000/api/products/'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
