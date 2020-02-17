from tastypie.resources import ModelResource
from app.models import Product, Category, Supplier


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = "product"


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"


class SupplierResource(ModelResource):
    class Meta:
        queryset = Supplier.objects.all()
        resource_name = "supplier"




