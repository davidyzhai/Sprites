#David Zhai
#1/17/2024
# This program interacts with a weather API, and takes in a city name and checks the current weather and temperature of the city.
# Not every city will work, but the API's database has over 200,000 cities
import requests
API_KEY = "e11a495ab2410b364de423c43d5ba245"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")