from django.db import models

# Create your models here.
class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    rate = models.IntegerField()
    city = models.CharField(max_length=30)