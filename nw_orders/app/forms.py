from django import forms


class CreateOrderForm(forms.Form):

    product = forms.CharField(label='Product', required=True)
    quantity = forms.IntegerField(label='Quantity', required=True)
    customer = forms.CharField(label='Customer', required=True)
    employee = forms.IntegerField(label='Employee', required=True)
    shipper = forms.IntegerField(label='Shipper', required=True)
    freight = forms.IntegerField(label='Freight', required=True)
