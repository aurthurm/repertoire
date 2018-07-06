from django.shortcuts import render
from products.resources import ItemResource
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import tablib, csv, os, path, io
from tablib import Dataset
from products.forms import ItemForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def upload_csv(request):
    if request.method == 'POST' and request.FILES['thefile']:
        paramFile = request.FILES['thefile'].read()
        fs = FileSystemStorage()
        filename = fs.save(request.FILES['thefile'].name, request.FILES['thefile'])
        uploaded_file_url = fs.url(filename)
        input = csv.DictReader(io.StringIO(paramFile.decode('utf-8')))
        list = []
        for row in input:
            list.append(row)

        i=0
        for line in list:
            data_dict = {}
            data_dict['name'] = list[i]['name']
            data_dict['departments'] = list[i]['departments']
            data_dict['image'] = list[i]['image']
            data_dict['description'] = list[i]['description']
            i+=1
            form = ItemForm(data_dict)
            if form.is_valid():
                form.save()

        return render(request, 'uploader/upload_csv.html')
    return render(request, 'uploader/upload_csv.html')

def export_csv(request):
    item_resource = ItemResource()
    dataset = item_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="items.csv"'
    return response

def export_json(request):
    item_resource = ItemResource()
    dataset = item_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="items.json"'
    return response

def export_xlsx(request):
    item_resource = ItemResource()
    dataset = item_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="items.xls"'
    return response
