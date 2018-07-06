import django_tables2 as tables
from .models import Adjustment, Transaction

class AdjustmentTable(tables.Table):

	class Meta:
		model = Adjustment
		# adds class="paleblue" to <table> tag
		attrs = {'class': 'paleblue'}

class TransactionTable(tables.Table):

	class Meta:
		model = Transaction
		# adds class="paleblue" to <table> tag
		attrs = {'class': 'paleblue'}