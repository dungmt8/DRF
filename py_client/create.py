import requests

endpoint = 'http://localhost:8000/api/products/create/'
headers = {
    'Authorization': 'Bearer dc98dfc1a0677fc87a3767731d077095d23e66b8'
}

data = {
    'title': 'lol',
    'price': 24.44
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
