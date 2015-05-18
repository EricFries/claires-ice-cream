import datetime

from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from IPython import embed

class IceCream(models.Model):
    flavor = models.CharField(max_length=30)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.flavor

class Topping(models.Model):
    variety = models.CharField(max_length=30)
    image_url = models.CharField(max_length=200)
    def __str__(self):
        return self.variety

class Container(models.Model):
    option = models.CharField(max_length=30)
    image_url = models.CharField(max_length=200)
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

    def send_emails(self):
        toppings = self.get_toppings()

        email_body = "%s\nOrder Details:\nFlavor: %s\nContainer: %s\nToppings: %s\n\nCustomer Information:\n %s\n%s\n%s\n%s\n " %(self.date, self.flavor.flavor, self.container.option, toppings, self.name, self.address, self.phone, self.email)

        send_mail("New Ice Cream Order!", email_body,
        "Claire's Ice Cream <ericfries@gmail.com>", ["ericfries@gmail.com"])

        send_mail("Order Confirmation", "Thanks for your order, %s!" %(self.name),
        "Claire's Ice Cream <ericfries@gmail.com>", [self.email])
