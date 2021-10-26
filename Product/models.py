from django.db import models


class Product(models.Model):
    picture = models.ImageField(upload_to='images', default='default.jpg')
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=15)

