from django.db import models

# Create your models here.
class drama(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=200)
    channel = models.CharField(max_length=100)
    info_url = models.TextField()
