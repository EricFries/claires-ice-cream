from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Order, IceCream

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Claire's Ice Cream!")


def flavor_list(request):
    return HttpResponse("Welcome to the flavor list!")

def topping_list(request):
    return HttpResponse("Welcome to the topping list!")

def container_list(request):
    return HttpResponse("Welcome to the container list!")