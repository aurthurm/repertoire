from django.db import models
from django.utils import timezone
from laboratory.models import Department, Supplier, Store
from django.core.validators import MinValueValidator

class Item(models.Model):
	name = models.CharField(max_length = 50, default = '',  unique = True)
	departments = models.ForeignKey('laboratory.Department', related_name = 'item_from', on_delete = models.PROTECT, blank = True, default = '')
	image = models.ImageField(null = True, blank = True)
	description = models.TextField(null = True, blank = True, default = '')

	def __str__(self):
		return self.name


class Category(models.Model):
	CATEGORIES = (
			('Consumables', 'Consumables'),
			('Reagents', 'Reagents'),
			('Durables', 'Durables')
		)
	name = models.CharField(max_length = 50, choices = CATEGORIES,  unique = True)
	description = models.TextField(null = True, blank = True, default = '')

	def __str__(self):
		return self.name

class Hazard(models.Model):
	HAZARDS = (
			('Caution', 'Caution'),
			('Toxic', 'Toxic'),
			('Very Toxic', 'Very Toxic'),
			('Corrosive', 'Corrosive'),
			('Irritant', 'Irritant'),
			('Harmful', 'Harmful'),
			('Flammable', 'Flammable'),
			('Highly Flammable', 'Highly Flammable'),
			('Biological', 'Biological'),
			('Electrical', 'Electrical'),
			('Explosive', 'Explosive'),
			('Oxidising', 'Oxidising'),
			('Environmental', 'Environmental'),
			('Reactive', ' Reactive'),
			('Physical', 'Physical'),
			('Mechanical', 'Mechanical'),
		)
	name = models.CharField(max_length = 50, choices = HAZARDS,  unique = True)
	description = models.TextField(null = True, blank = True, default = '')

	def __str__(self):
		return self.name

# Unit of Measurement
class Unit(models.Model):
	UNITS = (
			('l', 'liter'),
			('ml', 'milliliter'),
			('kg', 'kilogramme'),
			('g', 'gramme'),
			('mg', 'milligramme'),
			('ea', 'each'),
			('pc', 'piece'),
			('t', 'tonne'),
			('in', 'inch'),
			('cm', 'centimeter'),
			('m', 'meter'),
			('g', 'gallon'),
			('tests', 'tests'),
			('kit', 'kit')
		)
	name = models.CharField(max_length = 10, choices = UNITS, unique = True)

	def __str__(self):
		return self.name

class PackageType(models.Model):
	PACKAGINGS = (
			('box', 'box'),
			('container', 'container'),
			('bag', 'bag'),
			('plastic', 'plastic'),
			('bottle', 'bottle'),
			('bucket', 'bucket'),
			('tray', 'tray'),
			('crate', 'crate'),
			('bin', 'bin'),
			('pouche', 'pouche'),
			('envelope', 'envelope'),
			('kit', 'kit'),
			('cardboard', 'cardboard')
		)
	name = models.CharField(max_length = 10, choices = PACKAGINGS,  unique = True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.ForeignKey(Item, on_delete = models.PROTECT)
	department = models.ForeignKey('laboratory.Department', related_name = 'product_from',  on_delete = models.PROTECT, blank = True, default = '')
	supplier = models.ForeignKey('laboratory.Supplier', related_name = 'department_supplier',  on_delete = models.PROTECT, default = '')
	category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True, default = '', blank = True)
	hazard = models.ForeignKey(Hazard, on_delete = models.SET_NULL, null=True, default = '', blank = True)
	store = models.ForeignKey('laboratory.Store', related_name = 'product_bin' ,on_delete = models.PROTECT )
	lot_number = models.CharField(max_length = 20)
	batch = models.CharField(max_length = 20)
	size = models.DecimalField(decimal_places = 3, max_digits = 10)
	unit = models.ForeignKey(Unit, on_delete = models.PROTECT, default = '')
	packaging = models.ForeignKey(PackageType, on_delete = models.SET_NULL, null=True, default = '')
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default = 0.00, blank = True)
	quantity_received = models.PositiveIntegerField(default = 0, editable = True, validators=[MinValueValidator(1)])
	minimum_level = models.PositiveIntegerField(default = 0, editable = True, validators=[MinValueValidator(0)])
	remaining = models.PositiveIntegerField(default = 0, editable = True, validators=[MinValueValidator(0)])
	date_received = models.DateTimeField(default = timezone.now)
	expiry_date = models.DateField(default = timezone.now)
	received_by = models.ForeignKey('auth.User',  on_delete = models.PROTECT)

#	@property
	def maximum_level(self):
		return (self.minimum_level * 2)

	class Meta:
		unique_together = (
				('name', 'lot_number')
			)
		ordering = ('-date_received',)

	def __str__(self):
		# return str(str(self.name) + ' => ' + str(self.lot_number) + ' : ' + str(self.remaining))
		return str(str(self.name) + ' : ' + str(self.lot_number))
