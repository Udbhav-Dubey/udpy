import requests

# Coordinates for New Delhi
url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.21&current_weather=true"

response = requests.get(url)
data = response.json()

weather = data['current_weather']

print("📍 Location: New Delhi")
print(f"🌡️ Temperature: {weather['temperature']}°C")
print(f"🌬️ Wind Speed: {weather['windspeed']} km/h")
print(f"🕒 Time: {weather['time']}")

