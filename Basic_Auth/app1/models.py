from django.db import models

# Create your models here.
class praveen(models.Model):
    name= models.CharField(max_length=100)
    roll_num = models.IntegerField()
    age= models.IntegerField()

    def __str__(self):
        return self.name


