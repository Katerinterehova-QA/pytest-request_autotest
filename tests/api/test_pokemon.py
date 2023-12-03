import requests
import pytest


def test_status_code():
    url = "https://api.pokemonbattle.me:9104/trainers"
    response = requests.get(url)
    assert response.status_code ==200



def test_check_response():
    url = "https://api.pokemonbattle.me:9104/trainers"
    response = requests.get(url, params = {"trainer_id" : 3756})
    assert response.json()["trainer_name"] == "Екатерина"