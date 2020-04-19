from django.db import models


# Create your models here.
class Query(models.Model):
    title = models.CharField(max_length=30, default='Query')
    email = models.CharField(max_length=30, default='User')
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.message
