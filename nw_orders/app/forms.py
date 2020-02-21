from django import forms


class CreateOrderForm(forms.Form):

    product = forms.CharField(label='Product', required=True)
    quantity = forms.CharField(label='Quantity', required=True)
    customer = forms.CharField(label='Customer', required=True)
    employee = forms.CharField(label='Employee', required=True)
    shipper = forms.CharField(label='Shipper', required=True)
