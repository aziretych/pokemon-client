import requests


class Pokemon:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, name):
        response = requests.get(f"{self.BASE_URL}/{name}")

        if response.status_code == 200:
            data = response.json()

            print("\nPokemon Information")
            print("-------------------")
            print("Name:", data["name"])
            print("Height:", data["height"])
            print("Weight:", data["weight"])

        else:
            print("Pokemon not found")


pokemon = Pokemon()

name = input("Enter pokemon name: ").lower()

pokemon.get_pokemon(name)