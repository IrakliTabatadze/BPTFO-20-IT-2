import requests

character_url = 'https://rickandmortyapi.com/api/character'

response = requests.get(character_url).json()

print(response['results'])