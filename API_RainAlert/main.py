import requests

api_key="682268fad369e4af8092e0c4070c8490"

parameter = {
    "lat" : 5.3086262115819345,
    "lon" : 100.29261032409423,
    "appid" : api_key,
    "cnt" : 4,
    # "unit" : "metric",
}

proxies = {
    "http": "http://proxy-chain.intel.com:911",
    "https": "http://proxy-chain.intel.com:911",
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameter,
    proxies=proxies,
)

response.raise_for_status()
weather_data = response.json()
print(weather_data)

i=0
for hour_data in weather_data["list"]:
    weather_ID = hour_data["weather"][0]["id"]
    weather_hours = hour_data["dt_txt"]
    if weather_ID < 700:
        print(f"You will need umbrella at {weather_hours}")
    i += 1
