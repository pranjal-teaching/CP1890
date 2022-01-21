import requests


def get_all_weather_data(city="st. john's"):
    """
    Helper function. Makes a request to openweathermap server.
    :param city:
    :return: Returns entire current weather for the city.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "e3a3f627f93effe0dc13ea5ca84180c7"  # get your own https://home.openweathermap.org/api_keys
    url = f'{base_url}q={city}&appid={api_key}'
    resp = requests.get(url)
    return resp.json()


def get_current_temp_by_city(city):
    # return temp in Celsius
    data = get_all_weather_data(city)
    current_temp = data['main']['temp']
    return round(current_temp - 273.15)


def get_current_condition_by_city(city):
    # description
    data = get_all_weather_data(city)
    return data['weather'][0]['description']


def main():
    cities = ['St. John\'s', 'Toronto', 'Calgary', 'Corner Brook', 'Paris']
    for city in cities:
        print(f'Current Temp in {city}: {get_current_temp_by_city(city)} C.\tSummary: {get_current_condition_by_city(city)}')


if __name__ == '__main__':
    main()

"""
Returned Data format: 

coord  ->  {'lon': -52.7093, 'lat': 47.5649}
weather  ->  [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}]
base  ->  stations
main  ->  {'temp': 273.87, 'feels_like': 269.67, 'temp_min': 272.97, 'temp_max': 274.35, 'pressure': 1017, 'humidity': 84}
visibility  ->  2414
wind  ->  {'speed': 4.12, 'deg': 310}
snow  ->  {'1h': 0.25}
clouds  ->  {'all': 100}
dt  ->  1642767973
sys  ->  {'type': 2, 'id': 2035543, 'country': 'CA', 'sunrise': 1642763369, 'sunset': 1642796067}
timezone  ->  -12600
id  ->  6324733
name  ->  St. John's
cod  ->  200
"""