from django.db import models

# Create your models here.

class Order(models.Model):
    order_name = models.CharField(max_length=30)
    order_address = models.CharField(max_length=30)
    order_phone = models.CharField(max_length=30)
    order_email = models.CharField(max_length=30)
    order_date = models.DateTimeField('date ordered')