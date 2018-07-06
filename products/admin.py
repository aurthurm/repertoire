from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import *
from .forms import *
from ajax_select.admin import AjaxSelectAdmin
from import_export.admin import ImportExportModelAdmin

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']

class ItemAdmin(ImportExportModelAdmin):
	pass

class ProductAdmin(VersionAdmin, AjaxSelectAdmin):
	list_display = ('name', 'department', 'supplier', 'lot_number', 'batch', 'size', 'unit', 'packaging', 'quantity_received', 'minimum_level','maximum_level', 'remaining', 'expiry_date')
	form = ProductForm

admin.site.register(Item, ItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Unit)
admin.site.register(PackageType)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Hazard)
