from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import Authorization
from app.models import Product, Category, Supplier


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"
        filtering = {"category_name": ('exact', 'startswith',)}


class ProductResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, "category")

    class Meta:
        queryset = Product.objects.all()
        resource_name = "product"
        filtering = {"product_name": ('exact', 'startswith',), "category": ALL_WITH_RELATIONS}
        authorization = Authorization()


class SupplierResource(ModelResource):
    class Meta:
        queryset = Supplier.objects.all()
        resource_name = "supplier"
