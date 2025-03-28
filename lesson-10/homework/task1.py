import requests

API_KEY = "d6e8a5045d531ff62f221895001cf185"  # Replace with your actual API key
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL).json()

if "main" in response:
    temp = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    description = response["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description.capitalize()}")
else:
    print("Could not fetch weather data. Check your API key or try again later.")

