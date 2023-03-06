import requests

def get_weather_status(latitude, longitude):
    api_key = "b0e5a414003fe3e5899660e8900e0a0b"
    latitude = 80
    longitude = 100
    url = "https://api.openweathermap.org/data/2.5/weather?lat="+str(latitude)+"&lon="+str(longitude)+"&appid="+api_key
    response = requests.get(url)
    json = response.json()
    return {'description': json['weather'][0].get("description"),
            'temp_min': json.get('main').get('temp_min'),
            'temp_max': json.get('main').get('temp_max')
            }

def main():
    weather_dict = get_weather_status(80,100)
    # Printing the results
    print("Current weather is", weather_dict.get('description'))
    print("Min temperature",weather_dict.get('temp_min'))
    print("Max temperature",weather_dict.get('temp_max'))

main()