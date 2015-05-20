from django.test import TestCase
from .models import Order,IceCream,Topping,Container
from django.utils import timezone
# Create your tests here.

class OrderTestCase(TestCase):
    def setUp(self):
        Order.objects.create(name="Eric", address="11 Broadway, Ste. 200, New York, NY 10010", phone="555-555-5555", email="eric@eric.com", date=timezone.now())

    def test_order_has_name(self):
        eric = Order.objects.get(name="Eric")
        self.assertEqual(eric.name, 'Eric')
