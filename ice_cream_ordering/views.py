from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

from django.utils import timezone
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Order, IceCream, Topping, Container

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Claire's Ice Cream!")


def flavor_list(request):
    all_flavors = IceCream.objects.all()
    context = {'all_flavors': all_flavors}
    return render(request, 'ice_cream_ordering/flavors.html', context)

def topping_list(request):
    all_toppings = Topping.objects.all()
    context = {'all_toppings': all_toppings}
    return render(request, 'ice_cream_ordering/toppings.html', context)

def container_list(request):
    all_containers = Container.objects.all()
    context = {'all_containers': all_containers}
    return render(request, 'ice_cream_ordering/containers.html', context)