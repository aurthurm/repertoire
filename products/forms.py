from django import forms
from .models import *
from ajax_select.fields import AutoCompleteSelectField

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = { 'received_by': forms.HiddenInput(),  'remaining': forms.HiddenInput()   }

    name = AutoCompleteSelectField('items', required=False, help_text=None)

    def __init__( self, *args, **kwargs ):
        super(ProductForm, self).__init__( *args, **kwargs )
        self.fields['received_by'].label = "" #the trick to hide label:)
        self.fields['remaining'].label = ""

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class PackageForm(forms.ModelForm):

    class Meta:
        model = PackageType
        fields = '__all__'


class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = '__all__'


class HazardForm(forms.ModelForm):

    class Meta:
        model = Hazard
        fields = '__all__'
