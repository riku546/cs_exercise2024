from django.db import models
import time
# Create your models here.

class Article(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  posted_at = models.DateTimeField(default=time.timezone.now)
  published_at = models.DateTimeField(blank=True , null= True)
  like = models.IntegerField(default=0)