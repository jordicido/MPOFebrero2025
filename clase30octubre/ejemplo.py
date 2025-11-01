import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

if response.status_code == 200:
    data = response.json()
    print(data['name'])
    # for key, value in data.items():
    #     print(key)