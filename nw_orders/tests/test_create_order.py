from django.test import TestCase
from datetime import datetime
from app.models import Customer, Employee, Shipper, Order, OrderDetail
from app.config import PRODUCTS_SERVICE_URL
from app.rest_client import load_from_api_json
from app.products import product_result_handler


class OrderCreateTestCase(TestCase):

    def setUp(self):
        Customer.objects.create(customerid='TEST1',
                                company_name="IDM",
                                contact_name="Mr. Smith",
                                address="Ghencea 1, Bucuresti",
                                country="Romania")

        Employee.objects.create(employeeid=1001,
                                first_name="Alina",
                                last_name="Popescu",
                                title="Sales guy",
                                birth_date=datetime(1972, 10, 10),
                                hire_date=datetime(2012, 10, 10),
                                country="Romania",
                                postal_code="071242")

        Shipper.objects.create(shipperid=101,
                               company_name="FEDEX",
                               phone="0312121212")

    def test_create_order_no_details(self):
        customer = Customer.objects.get(pk='TEST1')
        employee = Employee.objects.get(pk=1001)
        shipper = Shipper.objects.get(pk=101)
        order = Order.objects.create(customer=customer,
                                     employee=employee,
                                     ship_via=shipper,
                                     order_date=datetime.now(),
                                     freight=14.5,
                                     ship_name="Order test",
                                     ship_city="Bucharest",
                                     ship_address="Ghencea 1, Bucuresti",
                                     ship_country="Romania"
                                     # ship_region="Test"
                                      )

    def test_create_order(self):
        customer = Customer.objects.get(pk='TEST1')
        employee = Employee.objects.get(pk=1001)
        shipper = Shipper.objects.get(pk=101)
        order = Order.objects.create(customer=customer,
                                     employee=employee,
                                     ship_via=shipper,
                                     order_date=datetime.now(),
                                     freight=14.5,
                                     ship_name="Order test",
                                     ship_city="Bucharest",
                                     ship_address="Ghencea 1, Bucuresti",
                                     ship_country="Romania"
                                      )

        products = load_from_api_json(PRODUCTS_SERVICE_URL, None, product_result_handler)
        order_detail = OrderDetail(product_id=products[0].id, quantity=5, order=order, unit_price=10)
        print(order_detail)
        order_detail = OrderDetail(product_id=products[1].id, quantity=7, order=order, unit_price=2)
        print(order_detail)