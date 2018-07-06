from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import *

class AdjustmentAdmin(VersionAdmin):
	list_display = ['product', 'adjustment_type', 'adjust']

class TransactionAdmin(VersionAdmin):
	list_display = ['product', 'issued', 'issued_to']

admin.site.register(Adjustment,AdjustmentAdmin)
admin.site.register(Transaction,TransactionAdmin)
