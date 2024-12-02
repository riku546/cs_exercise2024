from django.shortcuts import render
import random

# Create your views here.

def index(request):
  weathers = ['Sunny' , 'Rainy' , 'Cloudy' , 'Snowy']
  parms = {}
  parms['title'] = '3 days forecast'
  parms['forecasts'] = random.choices(weathers , k=3)
  return render(request , 'forecast/index.html', parms)