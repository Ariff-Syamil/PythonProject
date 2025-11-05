"""Use to check the weather by call API from https://openweathermap.org/forecast5"""
import requests
from datetime import datetime

Latitude = 5.161454
Longitude = 100.522243
API_KEYS = ""

OpenWeatherMap_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    'lat': Latitude,
    'lon': Longitude,
    'appid': API_KEYS,
    'cnt': 5
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
    weather = data["list"]
else:
    print("Request failed:", response.status_code)
    exit("Not 200 api response")

for days in weather:
    days_weather = days["weather"][0]["main"]
    date = days["dt_txt"]
    dt_object = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    day_name = dt_object.strftime("%A")

    # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    condition_codes = days["weather"][0]["id"]

    print(f"Date checked : {date}")
    print(f"This day will be on {day_name}")
    print(f"Weather in the day: {days_weather}")

    if days_weather == "Rain" or "Clouds" or condition_codes < 700:
        print("Bring umbrella today")
    else:
        print("Its a good day")

    print("\n")