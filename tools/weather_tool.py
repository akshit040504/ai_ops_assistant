import requests
import os

def get_weather(city):
    key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}"

    r = requests.get(url).json()

    if "current" not in r:
        return {"error": "Weather data not available"}

    return {
        "city": city,
        "temperature_c": r["current"].get("temp_c"),
        "condition": r["current"]["condition"]["text"],
        "humidity": r["current"].get("humidity")
    }

