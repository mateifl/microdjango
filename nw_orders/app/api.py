from tastypie.resources import ModelResource
from app.models import Order, Customer


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'


class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'
