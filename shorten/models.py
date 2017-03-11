from django.db import models

# Create your models here.
class UrlList(models.Model):
    url = models.URLField()
    short = models.CharField(max_length=10)
