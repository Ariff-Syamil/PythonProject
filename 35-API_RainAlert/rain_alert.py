"""Use to check the weather by call API from https://openweathermap.org/forecast5"""
import requests
import os
from datetime import datetime
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

Latitude = 5.161454
Longitude = 100.522243
API_KEYS = "682268fad369e4af8092e0c4070c8490"
# API_KEYS = os.environ.get("OPENWEATHER_API_KEYS")
account_sid = "ACbac2fed1a3ca61e53f20e4249c76d097"
# account_sid = os.environ.get("ACCOUNT_SID")
auth_token = "27313fc398e3f5c15c913aa1805da6fd"
# auth_token = os.environ.get("SID_AUTH")

OpenWeatherMap_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    'lat': Latitude,
    'lon': Longitude,
    'appid': API_KEYS,
    'cnt': 1
}

proxies = {
    "http": "http://proxy-chain.intel.com:911",
    "https": "http://proxy-chain.intel.com:911",
}

# proxies = {
#     'https': os.environ['https_proxy'],
#     'http':os.environ['http_proxy'],
# }

# proxy_client = TwilioHttpClient(
#     proxy=proxies,
# )

# client = Client(account_sid, auth_token, http_client=proxy_client)

# Example of API call
# https://api.openweathermap.org/data/2.5/weather?lat=5.161454&lon=100.522243&appid=682268fad369e4af8092e0c4070c8490

response = requests.get(
    OpenWeatherMap_Endpoint,
    params=parameters,
    # proxies=proxies,
    timeout=1200,
    )

if response.status_code == 200:
    data = response.json()
    weather = data["list"]
    print(weather)
else:
    print("Request failed:", response.status_code)
    exit("Not 200 api response")

for days in weather:
    days_weather = days["weather"][0]["main"]
    date = days["dt_txt"]
    dt_object = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    day_name = dt_object.strftime("%A")
    date_today = dt_object.strftime("%Y-%m-%d")

    # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    condition_codes = days["weather"][0]["id"]

    print(f"Date checked : {date_today}")
    print(f"This day will be on {day_name}")
    print(f"Weather in the day: {days_weather}")

    if days_weather == "Rain" or "Clouds" or condition_codes < 700:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'Date checked : {date_today}\nToday is {day_name}\nWeather in the day: {days_weather}\nBring 🌧️☂️ today',
            to='whatsapp:+60194442559',
        )
        print(message.sid)
    else:
        print("Its a good day")

    print("\n")