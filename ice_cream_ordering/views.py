from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Order, IceCream

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Claire's Ice Cream!")


def flavor_list(request):
    all_flavors = IceCream.objects.all()
    template = loader.get_template('ice_cream_ordering/flavors.html')
    context = RequestContext(request, {'all_flavors': all_flavors,
    	})
    return HttpResponse(template.render(context))

def topping_list(request):
    return HttpResponse("Welcome to the topping list!")

def container_list(request):
    return HttpResponse("Welcome to the container list!")