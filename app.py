import requests

# API Key from OpenWeatherMap
API_KEY = 'Enter API Key Here'

def get_weather(city_name):
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    response = requests.get(base_url)
    data = response.json()
    return data

city_name = input("Enter city name: ")
weather_data = get_weather(city_name)

if weather_data['cod'] == 200:
    weather_description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    
    print(f"Weather in {city_name}: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print("City not found")
