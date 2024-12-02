from django.contrib import admin
from django.urls import path , include
from myapp import views 
urlpatterns = [
  path('' , views.index , name = 'index'),
  path('<int:article_id>/update' , views.update , name='update'),
  path('hello' , views.hello , name='hello')
]