import os
from datetime import datetime
from api.weather import get_city_weather
def manipulate_html_file(params):
    file_path = "./index.html"
    for city in params:
        weather = get_city_weather(city)

        # Check if the file exists
        if not os.path.exists(file_path):
            # If it doesn't exist, create it
            with open(file_path, 'w') as file:
                file.write('Hello, this is a new file!')
        else:
            # Read the content of the HTML file
            with open(file_path, 'r') as file:
                lines = file.readlines()
            # Manipulate specific lines (replace 'old_text' with 'new_text')
            for i in range(len(lines)):

                if not lines[i].strip():
                    lines[i] = f"    <div id='weather-info'>\n        <h2>{weather['city_name']}</h2><img src='{weather['weather_icon']}'>\n        <p>Temperature: {weather['temp']} °C</p>\n        <p>Weather: {weather['weather']} - {weather['weather_description']}</p>\n        <p>Min. Temperature: {weather['temp_min']} °C</p>\n        <p>Max. Temperature: {weather['temp_max']} °C</p>\n        <p>Humidity: {weather['humidity']}%</p>\n        <p>Last update: {datetime.now()}</p>\n    </div>\n\n"
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)

    # Read the content of the file to delete the infos after send to S3
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Identify the range of lines to delete
    del lines[42:78]

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

