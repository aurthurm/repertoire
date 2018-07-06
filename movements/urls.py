from django.urls import path, re_path
from . import views
from django.views import generic
from .models import *

app_name = 'movements'

urlpatterns = [
    re_path(r'^stock/transaction/(?P<pk>\d+)/new/$', views.transaction_new, name = 'transaction_new'),
    path('stock/new/transaction/', views.new_transaction, name = 'new_transaction'),
    path('stock/transactions/', views.transactions, name = 'transactions'),
    re_path(r'^stock/adjustment/(?P<pk>\d+)/new/$', views.adjustment_new, name = 'adjustment_new'),
    path('stock/new/adjustment/', views.new_adjustment, name = 'new_adjustment'),
    path('stock/adjustment/', views.adjustments, name = 'adjustments'),
]
