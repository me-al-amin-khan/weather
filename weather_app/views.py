from django.shortcuts import render
import requests
from .models import City
from .forms import  CityForm

# Create your views here.

def index(request):

    cities = City.objects.all()


    # converted_temp_in_celcius = []

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=9b34addb86b961df273c4727aeaa723e'


    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate


    form = CityForm()

    weather_data = []


    # city = 'Dhaka'

    for city in cities:
            city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
            print(city_weather, type(city_weather))

            weather = {
                'city': city,
                'temparature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }

            weather_data.append(weather)



            # conv_temp = weather['temparature']
            # conv_temp = (conv_temp-32)*5/9
            # conv_temp = round(conv_temp, 2)
            #
            # print(conv_temp)

    # context = {'weather': weather, 'converted_temparature': conv_temp}



    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather_app/index.html', context)
