from django import forms
from .models import *

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = '__all__'

class LaboratoryForm(forms.ModelForm):

    class Meta:
        model = Laboratory
        fields = '__all__'

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = '__all__'

class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'

class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = '__all__'
