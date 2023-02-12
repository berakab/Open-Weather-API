from datetime import datetime
import requests 

base_url = "http://api.openweathermap.org/data/2.5/weather?"
API_key = open('api.txt','r').read()
CITY = input ("Enter the city name: ")

url = base_url + "appid=" + API_key + "&q=" + CITY

api_info = requests.get(url).json()

if api_info['cod'] == '404':
    print ("Invlaid City: {}, Please check your City Name".format(CITY))
else:
    temp_city = ((api_info['main']['temp']) - 273.15)
    weather_desc = api_info['weather'][0]['description']
    hdmt = api_info['main']['humidity']
    wind_spd = api_info['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("---------")
    print("Weather stats for - {} || {}".format(CITY.upper(), date_time))
    print ("----")

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc :",weather_desc)

    print ("Current Humdity : ",hdmt,'%')
    print ("Current wind speed :",wind_spd,'kmph')
