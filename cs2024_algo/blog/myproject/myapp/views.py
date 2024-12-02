from django.shortcuts import render
from django.http import HttpResponse
import random , time
# Create your views here.

def index(request):
    context = {
        "articles": [

        ]
    }
    
    return render(request, 'blog/index.html', context)





def hello(request):

  fortune_data = ['Great Fortune' , 'Small Fortune' , 'Bad Fortune']

  fortune_index = random.randint(0 , 3);

  data = {
    'name':'Alice',
    'weather':'CLOUDY',
    'weather_detail':['Temperature: 23℃','Humidity: 40%' , 'Wind: 5m/s'],
    'fortune': f'{fortune_data[fortune_index]}' ,
  }





  return render(request , 'blog/hello.html' , data)



def update(request , article_id):
  return HttpResponse(f'article_id:{article_id}')