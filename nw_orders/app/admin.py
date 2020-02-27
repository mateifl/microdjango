from django.contrib import admin
from app.models import Order, Customer, Employee


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'employee', 'order_date')


admin.site.register(Order)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'city', 'country')


admin.site.register(Customer)
admin.site.register(Employee)
