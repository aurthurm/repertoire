from django import forms
from .models import *

class TransactionForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TransactionForm, self).__init__(*args, **kwargs)
    #     self.fields['transaction_by'].widget = forms.HiddenInput()

    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = { 'transaction_by': forms.HiddenInput()  }

class AdjustmentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AdjustmentForm, self).__init__(*args, **kwargs)
    #     self.fields['adjustment_by'].widget = forms.HiddenInput()

    class Meta:
        model = Adjustment
        fields = '__all__'
        widgets = { 'adjustment_by': forms.HiddenInput()  }
