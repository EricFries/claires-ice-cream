from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flavors/$', views.flavor_list, name='flavor_list'),
    url(r'^toppings/$', views.topping_list, name='topping_list'),
    url(r'^containers/$', views.container_list, name='container_list')

]