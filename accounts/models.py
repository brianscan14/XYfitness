from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Attributes created for user's profile when they register"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, default='User')
    profile_pic = models.ImageField(
        upload_to='images',
        default='images/4648398-blue-steel.jpg'
    )

    def __str__(self):
        return self.username
