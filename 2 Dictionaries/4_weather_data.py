import requests

# construct URL to get weather info
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city = "st. john's"
api_key = "e3a3f627f93effe0dc13ea5ca84180c7" # https://home.openweathermap.org/api_keys
url = f'{base_url}q={city}&appid={api_key}'
print(url)

weather_data = requests.get(url)

# If code == 200, print all the data
if weather_data.status_code == 200:
    data = weather_data.json() # extract info from the response
    for key, value in data.items():
        print(f"{key} -> {value}")
elif weather_data.status_code == 404:
    print(f"City {city} not found")




def get_current_temp_by_city(city):
    # return temp in celcius
    pass

def get_current_condition_by_city(city):
    # description, feels like, wind etc.
    pass