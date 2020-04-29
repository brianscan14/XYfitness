from django.db import models
from products.models import Product


# below code taken from a Code Institute tutorial and modified for my project
class Order(models.Model):
    """Delivery detials of user who ordered item"""
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.IntegerField(blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(
        verbose_name=u'Town',
        max_length=40,
        blank=False
        )
    street_address1 = models.CharField(
        max_length=40,
        verbose_name=u'House name / apartment no (optional)',
        blank=True
        )
    street_address2 = models.CharField(
        max_length=40, verbose_name=u'Townland / street name', blank=False
        )
    county = models.CharField(
        max_length=40,
        verbose_name=u'County / city',
        blank=False
        )
    date = models.DateField()

    def __str__(self):
        return "{0}, {1}, {2}, {3} - ordered on {4}".format(
            self.id, self.full_name, self.country, self.county, self.date
        )


# below code taken from a Code Institute tutorial and modified for my project
class OrderLineItem(models.Model):
    """Returns items ordered in the admin app for this order"""
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price
            )
