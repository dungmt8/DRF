import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

data = {
    'title': 'fuck',
    'price': 30.11
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
