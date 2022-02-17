from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL

# Create your models here.


class client(models.Model):
    client_id = models.IntegerField(default=0, primary_key=True)
    client_address = models.CharField(max_length=250)
    client_name = models.CharField(max_length=50)
    client_age = models.IntegerField(default=0)
    client_illness = models.CharField(max_length=200)
    client_instrument = models.CharField(max_length=250)

    def __str__(self):
        return self.client_name

class situation(models.Model):
    progress = models.IntegerField(default=0)
    client_id = models.ForeignKey(client, on_delete=CASCADE, default="", primary_key=True)

    def __str__(self):
        return str(self.client_id)


class video(models.Model):
    video = models.FileField(upload_to="videos")