import requests
from django.shortcuts import render
from django.http import HttpResponse

API_KEY = 'bb0fd32a3dcf9b68b4d96e62af87cdc9'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def weather_report(request):
    context = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            context = {
                'city_name': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'humidity' : data['main']['temp'],
                'sea_level' : data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize(),
            }
        else:
            context['error'] = "City not found or an error occurred."

    return render(request, 'index.html', context)
