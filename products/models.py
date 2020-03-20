from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='images', default='XYfitness image')
    name = models.CharField(max_length=100, default='XYfitness Product')
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=30, default='plan or apparel')

    def __str__(self):
        return self.name
