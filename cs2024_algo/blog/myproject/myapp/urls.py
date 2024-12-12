from django.contrib import admin
from django.urls import path , include
from myapp import views 
urlpatterns = [
  path('' , views.index , name = 'index'),
  path('update/<int:article_id>/' , views.update , name='update'),
  path('detail/<int:article_id>/' , views.detail , name='detail'),
  path('delete/<int:article_id>/' , views.delete , name='delete'),
  path('hello' , views.hello , name='hello')
]