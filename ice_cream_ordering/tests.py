from django.test import TestCase
from .models import Order,IceCream,Topping,Container
from django.utils import timezone
# Create your tests here.

class IceCreamTestCase(TestCase):
    def setUp(self):
        chocolate = IceCream.objects.create(flavor="chocolate", image_url="http://www.somewhere.com")

    def test_icecream_has_flavor(self):
        chocolate = IceCream.objects.get(flavor="chocolate")
        self.assertEqual(chocolate.flavor, 'chocolate')

    def test_icecream_has_image_url(self):
        chocolate = IceCream.objects.get(flavor="chocolate")
        self.assertEqual(chocolate.image_url, "http://www.somewhere.com") 

class ContainerTestCase(TestCase):
    def setUp(self):
        cup = Container.objects.create(option="cup", image_url="http://www.somewhere.com")

    def test_container_has_option(self):
        cup = Container.objects.get(option="cup")
        self.assertEqual(cup.option, 'cup')
        
    def test_container_has_image_url(self):
        cup = Container.objects.get(option="cup")
        self.assertEqual(cup.image_url, "http://www.somewhere.com")

class ToppingTestCase(TestCase):
    def setUp(self):
        nuts = Topping.objects.create(variety="nuts", image_url="http://www.somewhere.com")

    def test_topping_has_variety(self):
        nuts = Topping.objects.get(variety="nuts")
        self.assertEqual(nuts.variety, 'nuts')
        
    def test_topping_has_image_url(self):
        nuts = Topping.objects.get(variety="nuts")
        self.assertEqual(nuts.image_url, "http://www.somewhere.com")       

class OrderTestCase(TestCase):
    def setUp(self):
        cup = Container.objects.create(option="cup", image_url="http://www.somewhere.com")
        chocolate = IceCream.objects.create(flavor="chocolate")
        Order.objects.create(name="Eric", address="11 Broadway, Ste. 200, New York, NY 10010", phone="555-555-5555", email="eric@eric.com", date=timezone.now(), flavor=chocolate, container=cup)

    def test_order_has_name(self):
        eric = Order.objects.get(name="Eric")
        self.assertEqual(eric.name, 'Eric')

    def test_order_has_address(self):
        eric = Order.objects.get(name="Eric")
        self.assertEqual(eric.address, "11 Broadway, Ste. 200, New York, NY 10010")

    def test_order_has_phone(self):
        eric = Order.objects.get(name="Eric")
        self.assertEqual(eric.phone, "555-555-5555")

    def test_order_has_container(self):
        eric = Order.objects.get(name="Eric")
        cup = eric.container
        self.assertEqual(eric.container, cup)

    def test_order_has_flavor(self):
        eric = Order.objects.get(name="Eric")
        chocolate = eric.flavor
        self.assertEqual(eric.flavor, chocolate)

    def test_order_can_have_toppings(self):
        eric = Order.objects.get(name="Eric")
        hotfudge = Topping.objects.create(variety="hot fudge")
        sprinkles = Topping.objects.create(variety="sprinkles")
        eric.toppings.add(hotfudge,sprinkles)
        self.assertEqual(eric.toppings.first(), hotfudge)
        self.assertEqual(eric.toppings.last(), sprinkles)