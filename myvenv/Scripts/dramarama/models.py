from django.db import models

# Create your models here.
class drama(models.Model):
    title = models.CharField(max_length=200)
    channel = models.CharField(max_length=100)
    info_url = models.TextField()
