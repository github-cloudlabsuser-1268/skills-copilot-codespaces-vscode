import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': 'api_key',
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

# Example usage:
api_key = '0d3986c326cc4aea83e8a13aef20777c'  # Replace with your actual API key
city = 'Kolkata'
weather_data = get_weather(city, api_key)
print(weather_data)