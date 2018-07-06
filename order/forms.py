from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['ordering_dept', 'order_by', 'order_number' ]
        widgets = { 'order_number': forms.HiddenInput()  }


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]
class OrderUpdateForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
