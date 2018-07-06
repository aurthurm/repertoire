from django.contrib import admin
from .models import *

class LaboratoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'mobile', 'phone', 'address', 'city', 'country']

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'laboratory')

class SupplierAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'mobile', 'phone', 'address', 'city', 'country')

admin.site.register(Country)
admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Store)
