import datetime

from django.db import models
from django.utils import timezone


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
    def __str__(self):
        return self.option

class Order(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=75)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    date = models.DateTimeField('date ordered')
    flavors = models.ManyToManyField(IceCream)
    topping = models.ForeignKey(Topping)
    container = models.ForeignKey(Container)

    def __str__(self):
        return self.name

    #returns a string of all ice cream flavors associated with an order 
    def get_flavors(self):
        l = []
        for f in self.flavors.all():
            l.append(f.flavor)
        return ", ".join(l)