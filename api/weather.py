import requests, os
from dotenv import load_dotenv

load_dotenv()

def get_lat_and_lon(city):
    url = "{}?q={}&limit=1&appid={}".format(os.environ.get("OPEN_WEATHER_API_GEOCODING_URL"), city, os.environ.get("OPEN_WEATHER_API_TOKEN"))

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
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

def get_weather(lat, lon):
    url = "{}?lat={}&lon={}&appid={}".format(os.environ.get("OPEN_WEATHER_API_WEATHER_URL"), lat, lon, os.environ.get("OPEN_WEATHER_API_TOKEN"))

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
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

def get_city_weather(city):
    coordinates = get_lat_and_lon(city)
    weather = get_weather(coordinates['lat'], coordinates['lon'])
    print(weather)


get_city_weather("Curitiba")
