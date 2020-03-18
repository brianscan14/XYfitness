from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Review(models.Model):
    title = models.CharField(max_length=30, default='Review Title')
    image = models.ImageField(upload_to='images', default='User image')
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
