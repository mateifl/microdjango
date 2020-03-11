from django import forms


class CreateOrderForm(forms.Form):

    product = forms.CharField(label='Product', required=True)
    quantity = forms.IntegerField(label='Quantity', required=True)
    customer = forms.IntegerField(label='Customer', required=True)
    employee = forms.IntegerField(label='Employee', required=True)
    shipper = forms.CharField(label='Shipper', required=True)
    ship_name = forms.CharField(label='Name', required=True)
    ship_country = forms.CharField(label='Country', required=True)
    ship_city = forms.CharField(label='City', required=True)
    address = forms.CharField(label='Address', required=True)
    freight = forms.IntegerField(label='Freight', required=True)
