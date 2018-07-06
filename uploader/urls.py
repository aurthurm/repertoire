from django.urls import path, re_path
from . import views
from django.views import generic
from .models import *

app_name = 'uploader'

urlpatterns = [
    re_path(r'^csv-export/$', views.export_csv, name='export_csv'),
    re_path(r'^csv/$', views.upload_csv, name='upload_csv'),
]
