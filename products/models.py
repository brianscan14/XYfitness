from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    image = models.ImageField(upload_to='images', default='XYfitness image')
    name = models.CharField(max_length=100, default='XYfitness Product')
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=30, default='plan or apparel')

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='Review Title')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
