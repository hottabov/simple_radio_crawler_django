from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200)
    bitrate = models.IntegerField()
    genre = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    site = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name