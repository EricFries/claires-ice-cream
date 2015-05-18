import datetime

from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from IPython import embed

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
    flavor = models.ForeignKey(IceCream)
    toppings = models.ManyToManyField(Topping)
    container = models.ForeignKey(Container)

    def __str__(self):
        return self.name

    #returns a string of all ice cream flavors associated with an order 
    def get_toppings(self):
        toppings_list = []
        for topping in self.toppings.all():
            toppings_list.append(topping.variety)
        return ", ".join(toppings_list)

    def send_email(self):
        toppings = self.get_toppings()

        email_body = "Order Details:\nFlavor: %s\nContainer: %s\nToppings: %s" %(self.flavor.flavor, self.container.option,toppings)

        send_mail("New Ice Cream Order!", email_body,
        "Djrill Sender <ericfries@gmail.com>", ["ericfries@example.com"])
