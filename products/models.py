from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    image = models.ImageField(upload_to='images', default='XYfitness image')
    name = models.CharField(max_length=100, default='XYfitness Product')
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    cats = (
        ('P', 'Plan'),
        ('A', 'Apparel'),
    )
    category = models.CharField(max_length=30, choices=cats, default='P')
    sizes = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    size = models.CharField(max_length=100, choices=sizes, default='choose size', verbose_name="size")

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='Review Title')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    ratings = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    rating = models.IntegerField(choices=ratings, default='5')

    def __str__(self):
        return self.title
