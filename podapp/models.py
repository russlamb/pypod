from django.db import models


# Create your models here.


class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    file = models.FileField(upload_to='episodes/')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    def __str__(self):
        return "{}-{}".format(self.podcast, self.title)

