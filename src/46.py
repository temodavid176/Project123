import requests
import json

def fetch_weather_data(city):
    url = f"https://api.weatherapi.com/v1/forecast.json?xml-version=latest&format=json&key={YOUR_API_KEY}&currency=USD&json=yahoo&country={city}%2C%20USA"
    response = requests.get(url)
    data = json.loads(response.text)
    
    # Extract and format the weather data
    temperature = data['result']['currentday']['feelslikec']
    weather_description = data['result']['currentday']['condition']['text']
    
    return {
        "temperature": temperature,
        "weather_description": weather_description
    }

city = "London"
weather_data = fetch_weather_data(city)
print(weather_data)
