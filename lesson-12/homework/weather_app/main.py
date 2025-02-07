import requests
import os 

api_key = os.environ.get('WEATHER_API_KEY')




def get_loc(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    return requests.get(url).json()

def get_info(lat, lon):
    url = f'https://api.openweathermap.org/data/3.0/onecalllat={lat}&lon={lon}&appid={api_key}'
    return requests.get(url).json()




city = input("Input name of a city: ")
loc = get_loc(city)
if not loc:
    print("No city found.")
    exit(0)

lat = loc[0]['lat']
lon = loc[0]['lon']
info = get_info(lat, lon)

temp = inf[0]['main']['temp'] - 273.15
print(f"Temperature in {loc[0]['name']} is {temp:.2f} ˚C")