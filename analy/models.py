from django.db import models

class weather_data(models.Model):

    place = models.CharField(max_length=30)
    wind_direction = models.CharField(max_length=30)
    wind_speed = models.TextField(max_length=10)
    astronomy = models.CharField(max_length=30)
    date = models.CharField(max_length=30,default="")
    time = models.TextField(max_length=10)
    temp = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30,default='null')
    presure = models.CharField(max_length=30,default='null')
    visibility = models.CharField(max_length=30,default='null')

    def __str__(self):
        return self.time
# Create your models here.
class pre(models.Model):
    place = models.TextField(max_length=30,default="")
    temp = models.TextField(max_length=30,default='0')
    date = models.TextField(max_length=30,default='')
    wind = models.TextField(max_length=30,default='0')
    presure = models.CharField(max_length=30,default='0')
    humidity = models.CharField(max_length=30,default='0')

    def __str__(self):
        return self.place