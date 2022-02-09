from django.db import models

# Create your models here.
class student_model(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    age = models.IntegerField()