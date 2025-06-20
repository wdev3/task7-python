import requests
import os

pokemon_name = input("Enter the name of the Pokémon you want to search:\n").lower()
os.system("cls")
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
response = requests.get(url)
pokemon_data = response.json()

print(pokemon_data['name'])
print(pokemon_data['height'])
print(pokemon_data['weight'])
print(pokemon_data['types'][0]['type']['name'])
print(pokemon_data['sprites']['front_default'])
