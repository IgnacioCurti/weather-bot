import requests
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/"


def get_current_weather(city = "Rosario"):
    params = {
        "key": API_KEY,
        "q": city
    }
    request = requests.get(BASE_URL + "current.json", params = params).json()
    if request.get('error'):
        return request.get('error').get('message')
    current_wheater = request.get("current")
    capitalized_city = ' '.join([x.capitalize() for x in city.split(' ')])
    return f"Current wheater in {capitalized_city} (last updated: {current_wheater.get('last_updated')}): {current_wheater.get('temp_c')} °C, {current_wheater.get('condition').get('text')}. Humidity: {current_wheater.get('humidity')}%. Feels like: {current_wheater.get('feelslike_c')} °C."
