import requests
import pytest

URL="https://api.pokemonbattle.me/v2"
HEADERS={"Content-Type":"application/json"}
TOKEN="b1ef30dbf3760e503f3445c04d607f50"


def test_status_code():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id' :2401})
    assert response.status_code==200

def test_name_trainer_correct():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id' :2401})
    assert response.json()['data'][0]['trainer_name']=='ArtemKa'