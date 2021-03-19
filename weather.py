import requests

def InfoByCity(city,APIKEY):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,APIKEY)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    iconcode = data['weather'][0]['icon']
    iconurl = "http://openweathermap.org/img/w/" + iconcode + ".png"
    return temp,iconurl