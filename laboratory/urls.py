from django.urls import path, re_path
from . import views
from django.views import generic
from .models import *

app_name = 'laboratory'

urlpatterns = [
    path('suppliers/', views.suppliers, name='suppliers'),
    re_path(r'^supplier/(?P<pk>\d+)/$', views.supplier_detail, name = 'supplier_detail'),
    path('supplier/new/', views.supplier_new, name = 'supplier_new'),
    re_path(r'^supplier/(?P<pk>\d+)/edit/$', views.supplier_edit, name='supplier_edit'),
    re_path(r'^supplier/(?P<pk>\d+)/remove/$', views.supplier_remove, name='supplier_remove'),
    path('stores/', views.stores, name='stores'),
    re_path(r'^store-detail/(?P<pk>\d+)/$', views.store_detail, name = 'store_detail'),
    path('store/new/', views.store_new, name = 'store_new'),
    re_path(r'^store/(?P<pk>\d+)/edit/$', views.store_edit, name='store_edit'),
    re_path(r'^store/(?P<pk>\d+)/remove/$', views.store_remove, name='store_remove'),
    path('countries/', views.countries, name='countries'),
    re_path(r'^country-detail/(?P<pk>\d+)/$', views.country_detail, name = 'country_detail'),
    path('country/new/', views.country_new, name = 'country_new'),
    re_path(r'^country/(?P<pk>\d+)/edit/$', views.country_edit, name='country_edit'),
    re_path(r'^country/(?P<pk>\d+)/remove/$', views.country_remove, name='country_remove'),
    path('laboratories/', views.laboratories, name='laboratories'),
    re_path(r'^lab/(?P<pk>\d+)/$', views.laboratory_detail, name = 'laboratory_detail'),
    path('lab/new/', views.laboratory_new, name = 'laboratory_new'),
    re_path(r'^lab/(?P<pk>\d+)/edit/$', views.laboratory_edit, name='laboratory_edit'),
    re_path(r'^lab/(?P<pk>\d+)/remove/$', views.laboratory_remove, name='laboratory_remove'),
    path('departments/', views.departments, name='departments'),
    re_path(r'^departments-list/$', views.departments_list, name='departments_list'),
    re_path(r'^department-detail/(?P<pk>\d+)/$', views.department_detail, name = 'department_detail'),
    path('department/new/', views.department_new, name = 'department_new'),
    re_path(r'^department/(?P<pk>\d+)/edit/$', views.department_edit, name='department_edit'),
    re_path(r'^department/(?P<pk>\d+)/remove/$', views.department_remove, name='department_remove'),
]
