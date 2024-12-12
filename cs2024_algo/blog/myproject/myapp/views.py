from django.shortcuts import render , redirect
from django.http import HttpResponse
import random , time
from myapp.models import Article
from django.http import Http404
# Create your views here.

def index(request):
    
    if request.method == 'POST':
       article = Article(title = request.POST['title'] , body = request.POST['text'])
       article.save()
       return redirect(detail , article.id)

    context = {
        "articles":Article.objects.all()
    }
    
    return render(request, 'blog/index.html', context)


def update(request , article_id):
   try:
      article = Article.objects.get(pk = article_id)
   except Article.DoesNotExist:
      raise Http404('Article does not exist')
   
   if request.method == 'POST':
      article.title = request.POST['title']
      article.body = request.POST['text']
      article.save()
      return redirect(detail , article_id)
   return render(request , 'blog/edit' , {'article':article})


def detail(request , article_id):
   try:
      article = Article.objects.get(pk=article_id)
   except Article.DoesNotExist:
      raise Http404('Article does not exist')
   
   return render(request , 'blog/detail.html' , {'article':article})

    
def delete(request , article_id):
   try:
      article = Article.objects.get(pk=article_id)
   except Article.DoesNotExist:
      raise Http404('Article does not exist')
   
   article.delete()

   return redirect(index)







