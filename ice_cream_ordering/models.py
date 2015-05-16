import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
#add foreign keys to order instead?
# 1 flavor, 1 conatiner, multiple toppings

class Order(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=75)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    date = models.DateTimeField('date ordered')
    flavor = models.ForeignKey(IceCream)
    topping = models.ForeignKey(Topping)
    container = models.ForeignKey(Container)

    def __str__(self):
        return self.name

class IceCream(models.Model):
    flavor = models.CharField(max_length=30)
    def __str__(self):
        return self.flavor

class Topping(models.Model):
    variety = models.CharField(max_length=30)
    def __str__(self):
        return self.variety

class Container(models.Model):
    option = models.CharField(max_length=30)