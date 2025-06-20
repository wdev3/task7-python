# Introduction to Requests Training

This Python script is a basic exercise to practice using the **requests** library and consuming data from a public API (PokéAPI).

The program asks for a Pokémon name and returns information such as the name, height, weight, main type, and the URL of the Pokémon's image.

---

## Code Explanation

- The program asks the user to enter the name of the Pokémon they want to search.
- It clears the terminal screen for better visualization.
- It constructs a dynamic URL to access the PokéAPI using the given Pokémon name.
- It makes an HTTP GET request to fetch the Pokémon data.
- If successful, it prints:
  - Pokémon name
  - Height
  - Weight
  - Main type
  - URL of the Pokémon's front image (sprite)

---

## Technologies used

- Python 3  
- `requests` library for HTTP requests  
- Public API: PokéAPI (https://pokeapi.co/)

---

## How to use

1. Make sure you have Python 3 installed.  
2. Install the `requests` library if you don't have it yet:  
