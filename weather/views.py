import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=4e78fa71de97f97aa376e42f2f1c99cf'

    city = 'London'
    res = requests.get(url.format(city))
    print(res.text)
    return render(request, 'weather/index.html')
