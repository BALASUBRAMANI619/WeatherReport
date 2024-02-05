from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    city = 'London'  # Replace with the desired city name
    api_key = 'feaaaf970df86af3e97972e4c09330a2'  # Replace with your OpenWeatherMap API key

    # Make API request to OpenWeatherMap
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        return render_template('index.html', city=city, temperature=temperature, weather_description=weather_description)
    else:
        return f'Error fetching weather data. Status code: {response.status_code}'
    

@app.route('/json')
def json():
    city = 'Mumbai'  # Replace with the desired city name
    api_key = 'feaaaf970df86af3e97972e4c09330a2'  # Replace with your OpenWeatherMap API key

    # Make API request to OpenWeatherMap
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"Printing variable 'data': {weather_data}")
        return render_template('json.html', weather_data=weather_data)
    else:
        return f'Error fetching weather data. Status code: {response.status_code}'
if __name__ == '__main__':
    app.run(debug=True)
