import requests


URL="https://api.pokemonbattle.me/v2"
HEADERS={"Content-Type":"application/json","trainer_token":"b1ef30dbf3760e503f3445c04d607f50"}
TOKEN="b1ef30dbf3760e503f3445c04d607f50"

body={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response=requests.post(url=f"{URL}/pokemons", headers=HEADERS, json=body)

print(response.text)


response=requests.put(url=f"{URL}/pokemons", headers=HEADERS, json={
    "pokemon_id": "16319",
    "name": "qa studio",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response.text)




response=requests.post(url=f"{URL}/trainers/add_pokeball", headers=HEADERS, json={
    "pokemon_id": "16319"
})

print(response.text)







