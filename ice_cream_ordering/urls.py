from django.conf.urls import url

from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flavors/$', views.flavor_list, name='flavor_list'),
    url(r'^toppings/$', views.topping_list, name='topping_list'),
    url(r'^containers/$', views.container_list, name='container_list'),
		url(r'^new/$', views.new, name='new'),
		url(r'^create/$', views.create, name='create')
]

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )