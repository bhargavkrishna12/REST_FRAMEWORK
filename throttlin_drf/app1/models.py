from django.db import models

# Create your models here.

class Movies(models.Model):
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=40)
    location = models.CharField(max_length=100)
