from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_number', 'order_by', 'ordering_dept', 'created']
    list_filter = ['order_state', 'created', 'updated']
    inlines = [OrderProductInline]

admin.site.register(Order, OrderAdmin)
