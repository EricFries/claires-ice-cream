from django.contrib import admin

from .models import Order, IceCream, Topping, Container
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(Order)
admin.site.register(IceCream)
admin.site.register(Topping)
admin.site.register(Container)