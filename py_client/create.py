import requests

endpoint = 'http://localhost:8000/api/products/create/'

data = {
    'title': 'lol',
    'price': 24.44
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
