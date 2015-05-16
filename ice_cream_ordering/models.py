from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=75)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    date = models.DateTimeField('date ordered')

    def __str__(self):
        return self.order_name

class IceCream(models.Model):
    order = models.ForeignKey(Order)
    flavor = models.CharField(max_length=30)

class Topping(models.Model):
    order = models.ForeignKey(Order)
    variety = models.CharField(max_length=30)