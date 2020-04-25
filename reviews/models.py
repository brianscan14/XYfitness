from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Review(models.Model):
    """Fields used for a testimonial the user can add to the site."""
    title = models.CharField(max_length=30, default='Review Title')
    image = models.ImageField(
        upload_to='images', default='images/4648398-blue-steel.jpg'
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    content = models.TextField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    before_picture = models.ImageField(
        upload_to='images',
        blank=True,
        verbose_name=u"Before pic (only add these if you want to)."
    )
    after_picture = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title
