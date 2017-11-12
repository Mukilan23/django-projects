from django.db import models

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)


class Songs(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    singer=models.CharField(max_length=250)
