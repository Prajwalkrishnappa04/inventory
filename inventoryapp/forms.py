from django import forms
from .models import Item, PurchaseItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'stock']

class PurchaseForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    customer_address = forms.CharField(widget=forms.Textarea)

class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['item', 'quantity']
