from django.db import models
from django.utils import timezone
from products.models import Product
from laboratory.models import Department


# transactions are issues
class Transaction(models.Model):
	product = models.ForeignKey('products.Product', related_name = 'product_transaction', on_delete = models.PROTECT)
	issued = models.IntegerField(default = 0)
	issued_to = models.ForeignKey('laboratory.Department', related_name = 'dpt_issued_to', on_delete = models.PROTECT)
	date_issued = models.DateTimeField(default=timezone.now)
	transaction_by = models.ForeignKey('auth.User', on_delete = models.PROTECT)

	class Meta:
		ordering = ('-date_issued',)

	def __str__(self):
		return str(self.product)

class Adjustment(models.Model):
	product = models.ForeignKey('products.Product', related_name = 'product_adjustment', on_delete = models.PROTECT)
	ADJUST = (
			('TRANSFER IN', 'TRANSFER IN'),
			('TRANSFER OUT', 'TRANSFER OUT'),
			('DAMAGED', 'DAMAGED'),
			('EXPIRED', 'EXPIRED'),
			('THEFT', 'THEFT'),
			('LOSS', 'LOSS'),
		)
	adjustment_type = models.CharField(max_length = 15, choices = ADJUST)
	adjust = models.IntegerField(default = 0)
	adjustment_date = models.DateTimeField(default=timezone.now)
	remarks = models.TextField(default='')
	adjustment_by = models.ForeignKey('auth.User', on_delete = models.PROTECT)

	class Meta:
		ordering = ('-adjustment_date',)

	def __str__(self):
		return str(self.product)
