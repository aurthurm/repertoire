from django.conf.urls import url
from . import views

app_name = 'order'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^orders-processed/$', views.processed_orders, name='processed_orders'),
    url(r'^orders/$', views.orders, name='orders'),
    url(r'^detail/(?P<order_id>\d+)/$', views.view_order, name='view_order'),
    url(r'^(?P<order_id>\d+)/processed/$', views.process_order, name='process_order'),
]
