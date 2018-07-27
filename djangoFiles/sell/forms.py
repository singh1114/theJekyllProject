from django import forms

from gcproduct.models import Item

from sell.models import Customer


class SellProductForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all())
    quantity = forms.DecimalField(decimal_places=2, max_digits=10)
