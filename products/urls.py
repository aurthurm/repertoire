from django.urls import path, re_path
from . import views
from django.views import generic
from .models import *


app_name = 'products'

urlpatterns = [
    path('search/', views.ProductSearchListView.as_view(), name='product_search_list'),
    re_path(r'^search/items/$', views.ItemSearchListView.as_view(), name='item_search_list'),

    path('stocks/', views.stocks, name='stocks'),
    re_path(r'^dep-(?P<department_id>\d+)/stock-detail/(?P<pk>\d+)/$', views.stock_detail, name = 'stock_detail'),
    re_path(r'^dep-(?P<department_id>\d+)/stock/new/', views.stock_new, name = 'stock_new'),
    re_path(r'^stock/(?P<pk>\d+)/edit/$', views.stock_edit, name='stock_edit'),
    re_path(r'^stock/(?P<pk>\d+)/remove/$', views.stock_remove, name='stock_remove'),
    path('stock/outs/', views.out_of_stock, name = 'out_of_stock'),
    path('stock/minimum/', views.at_minimum_stock, name = "at_minimum_stock"),
    path('stock/approaching-minimum-stock/', views.approaching_minimum_stock, name = "approaching_minimum_stock"),
    path('stock/below-minimum-stock/', views.below_minimum_stock, name = "below_minimum_stock"),
    path('stock/over-maximum-stock/', views.over_maximum_stock, name = "over_maximum_stock"),
    path('stock/expired/', views.expired_stock, name = "expired_stock"),
    path('stock/expiring-today/', views.expire_today_stock, name = "expire_today_stock"),
    path('stock/expire-this-week/', views.expire_this_week_stock, name = "expire_this_week_stock"),
    path('stock/expire-this-month/', views.expire_this_month_stock, name = "expire_this_month_stock"),
    re_path(r'^department/(?P<department_id>\d+)/$', views.departmental_stocks, name = 'departmental_stocks'),

    re_path(r'^item/(?P<pk>\d+)/$', views.departmental_items, name = 'departmental_items'),
    path('items/', views.items, name='items'),
    re_path(r'^item-detail/(?P<pk>\d+)/$', views.item_detail, name = 'item_detail'),
    path('item/new/', views.item_new, name = 'item_new'),
    re_path(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    re_path(r'^item/(?P<pk>\d+)/remove/$', views.item_remove, name='item_remove'),

    path('categories/', views.categories, name='categories'),
    re_path(r'^category-detail/(?P<pk>\d+)/$', views.category_detail, name = 'category_detail'),
    path('category/new/', views.category_new, name = 'category_new'),
    re_path(r'^category/(?P<pk>\d+)/edit/$', views.category_edit, name='category_edit'),
    re_path(r'^category/(?P<pk>\d+)/remove/$', views.category_remove, name='category_remove'),

    path('packages/', views.packages, name='packages'),
    re_path(r'^package-detail/(?P<pk>\d+)/$', views.package_detail, name = 'package_detail'),
    path('package/new/', views.package_new, name = 'package_new'),
    re_path(r'^package/(?P<pk>\d+)/edit/$', views.package_edit, name='package_edit'),
    re_path(r'^package/(?P<pk>\d+)/remove/$', views.package_remove, name='package_remove'),

    path('units/', views.units, name='units'),
    re_path(r'^unit-detail/(?P<pk>\d+)/$', views.unit_detail, name = 'unit_detail'),
    path('unit/new/', views.unit_new, name = 'unit_new'),
    re_path(r'^unit/(?P<pk>\d+)/edit/$', views.unit_edit, name='unit_edit'),
    re_path(r'^unit/(?P<pk>\d+)/remove/$', views.unit_remove, name='unit_remove'),

    path('hazards/', views.hazards, name='hazards'),
    re_path(r'^hazard-detail/(?P<pk>\d+)/$', views.hazard_detail, name = 'hazard_detail'),
    path('hazard/new/', views.hazard_new, name = 'hazard_new'),
    re_path(r'^hazard/(?P<pk>\d+)/edit/$', views.hazard_edit, name='hazard_edit'),
    re_path(r'^hazard/(?P<pk>\d+)/remove/$', views.hazard_remove, name='hazard_remove'),
]
