"""Use to check the weather by call API from https://openweathermap.org/current"""
import requests

Latitude = 5.161454
Longitude = 100.522243
API_KEYS = "682268fad369e4af8092e0c4070c8490"

OpenWeatherMap_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    'lat': Latitude,
    'lon': Longitude,
    'appid': API_KEYS,
}

proxies = {
    "http": "http://proxy-chain.intel.com:911",
    "https": "http://proxy-chain.intel.com:911",
}

# Example of API call
# https://api.openweathermap.org/data/2.5/weather?lat=5.161454&lon=100.522243&appid=682268fad369e4af8092e0c4070c8490

response = requests.get(
    OpenWeatherMap_Endpoint,
    params=parameters,
    proxies=proxies,
    # timeout=1200
    )

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed:", response.status_code)
