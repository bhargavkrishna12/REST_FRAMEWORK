from django.db import models

# Create your models here.

class Movies_list(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_loc = models.CharField(max_length=100)
    movie_Release = models.DateTimeField()
    ticket_cost = models.IntegerField()
    movie_rating = models.IntegerField()