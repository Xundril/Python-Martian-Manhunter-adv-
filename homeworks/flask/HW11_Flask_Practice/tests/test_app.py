import pytest
import json

from conftest import client
from config import Config


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "eb693de49dmsh5020a2f638740f4p1f0889jsnf4b5bc7fbd2f"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"cities": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


def test_search_weather_m(client, mocker):
    mocker.patch('requests.request', side_effect=ApiMock)
    response = client.post("/search", data={"cities": "Kiev"})
    print(response)
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


class ApiMock:
    def __init__(self, *args, **kwargs):
        self.data_ = {'message': 'accurate', 'cod': '200', 'count': 1, 'list': [
            {'id': 2643743, 'name': 'London', 'coord': {'lat': 51.5085, 'lon': -0.1257},
             'main': {'temp': 298.82, 'feels_like': 298.33, 'temp_min': 297.59, 'temp_max': 299.82, 'pressure': 1020,
                      'humidity': 34}, 'dt': 1623258571, 'wind': {'speed': 4.63, 'deg': 240}, 'sys': {'country': 'GB'},
             'rain': None, 'snow': None, 'clouds': {'all': 20},
             'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}]}
        self.status_code = 200

    def json(self):
        return self.data_