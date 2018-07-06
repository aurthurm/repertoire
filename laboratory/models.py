from django.db import models

class Country(models.Model):
	name = models.CharField(max_length = 50, default = 'Zimbabwe',  unique = True)

	def __str__(self):
		return self.name

class Laboratory(models.Model):
	name = models.CharField(max_length = 100, default = 'Bulawayo Group Laboratory')
	country = models.ForeignKey(Country, on_delete = models.PROTECT, blank = True, default =  '',)
	email = models.EmailField(blank = True, null = True)
	mobile = models.IntegerField(blank = True, null = True)
	phone = models.IntegerField(blank = True, null = True)
	address = models.TextField()
	city = models.CharField(max_length = 20)

	class Meta:
		unique_together = ('name', 'country')

	def __str__(self):
		return self.name


class Store(models.Model):
	name = models.CharField(max_length = 50, default = '',  unique = True)
	description = models.TextField(null = True, blank = True, default = '')

	def __str__(self):
		return self.name

class Department(models.Model):
	laboratory = models.ForeignKey(Laboratory, on_delete = models.PROTECT, default = '')
	DEPARTMENTS = (
			('BGL Laboratory', 'BGL Laboratory'),
			('Haematology', 'Haematology'),
			('Chemistry', 'Chemistry'),
			('Bacteriology', 'Bacteriology'),
			('Parasitology', 'Parasitology'),
			('Blood Bank', 'Blood Bank'),
			('Histopathology', 'Histopathology'),
			('HIV', 'HIV'),
			('Immunology', 'Immunology'),
			('Serology', 'Serology'),
			('Immuno-Hematology', 'Immuno-Hematology'),
		)
	name = models.CharField(max_length = 20, choices = DEPARTMENTS, unique = True)

	class Meta:
		unique_together = ('laboratory', 'name', )

	def __str__(self):
		return self.name

class Supplier(models.Model):
	name = models.CharField(max_length = 50, default = '')
	country = models.ForeignKey(Country, on_delete = models.PROTECT, default = 'Zimbabwe')
	email = models.EmailField(blank = True, null = True)
	mobile = models.IntegerField(blank = True, null = True)
	phone = models.IntegerField(blank = True, null = True)
	address = models.TextField()
	city = models.CharField(max_length = 100)

	class Meta:
		unique_together = ('name', 'country')

	def __str__(self):
		return self.name
