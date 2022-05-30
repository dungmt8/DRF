from getpass import getpass
import requests


product_id = input("What is the product id you want to get? ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

auth_endpoint = 'http://localhost:8000/api/auth/'
username = input('What is your username? ')
password = getpass('What is your password? ')
data = {
    'username': username,
    'password': password
}

auth_response = requests.post(auth_endpoint, json=data)
print(auth_response.json())

if product_id and auth_response.status_code == 200:
    endpoint = f'http://localhost:8000/api/products/{product_id}'
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
