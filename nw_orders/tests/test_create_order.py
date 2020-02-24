from django.test import TestCase
from datetime import datetime
from app.models import Customer, Employee, Shipper, Order, OrderDetail


class OrderCreateTestCase(TestCase):

    def setup(self):
        Customer.objects.create(customer_id = 'TEST1',
                                company_name = "IDM",
                                contact_name = "Mr. Smith",
                                address = "Ghencea 1, Bucuresti",
                                country = "Romania")

        Employee.objects.create(employee_id = 10,
                                first_name = "Alina",
                                last_name = "Popescu",
                                title = "Sales guy",
                                birth_date = datetime(1972, 10, 10),
                                hire_date = datetime(2012, 10, 10)),
                                country = "Romania",
                                postal_code = "071242" )
        Shipper.objects.create(shipper_id = 101,
                               company_name = "FEDEX",
                               phone = "0312121212")

    def test_create_order(self):
        customer = Customer.objects.get(pk='TEST1')
        employee = Employee.objects.get(pk=10)
        shipper = Shipper.objects.get(pk=10)
