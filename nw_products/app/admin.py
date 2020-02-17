from django.contrib import admin
from app.models import Product, Category, Supplier

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'unit_price', 'discontinued')

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

admin.site.register(Category, CategoryAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name')

admin.site.register(Supplier, SupplierAdmin)
