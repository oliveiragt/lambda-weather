import requests, os
from dotenv import load_dotenv

load_dotenv()

def get_lat_and_lon(city):
    url = "{}?q={}&limit=1&appid={}&units=metric".format(os.environ.get("OPEN_WEATHER_API_GEOCODING_URL"), city, os.environ.get("OPEN_WEATHER_API_TOKEN"))

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        
        # If the code reaches this point, the request was successful
        data = response.json()  # If the response contains JSON data
        result = {
            "lat": "{}".format(data[0]["lat"]),
            "lon": "{}".format(data[0]["lon"])
        }
        return result

    except requests.exceptions.HTTPError as err:
        return f"HTTP Error: {err}"
    except requests.exceptions.RequestException as err:
        return f"Request Error: {err}"

def get_weather(lat, lon):
    url = "{}?lat={}&lon={}&appid={}&units=metric".format(os.environ.get("OPEN_WEATHER_API_WEATHER_URL"), lat, lon, os.environ.get("OPEN_WEATHER_API_TOKEN"))

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        
        # If the code reaches this point, the request was successful
        data = response.json()  # If the response contains JSON data
        return data

    except requests.exceptions.HTTPError as err:
        return f"HTTP Error: {err}"
    except requests.exceptions.RequestException as err:
        return f"Request Error: {err}"

def get_city_weather(city):
    coordinates = get_lat_and_lon(city)
    weather = get_weather(coordinates['lat'], coordinates['lon'])
    result = {
        "city_name": "{}".format(weather["name"]),
        "weather": "{}".format(weather["weather"][0]["main"]),
        "weather_description": "{}".format(weather["weather"][0]["description"]),
        "weather_icon": "https://openweathermap.org/img/wn/{}@2x.png".format(weather["weather"][0]["icon"]),
        "temp": "{}".format(int(weather["main"]["temp"])),
        "temp_min": "{}".format(int(weather["main"]["temp_min"])),
        "temp_max": "{}".format(int(weather["main"]["temp_max"])),
        "humidity": "{}".format(weather["main"]["humidity"])
    }
    return result