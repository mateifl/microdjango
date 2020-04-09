from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from app.models import Customer, Employee, Shipper, Order, OrderDetail
from app.config import PRODUCTS_SERVICE_URL
from app.rest_client import load_from_api_json, update
from app.products import product_list_result_handler, check_stock
from app.logging import LoggerMixin
import json


class OrderCreateTestCase(TestCase, LoggerMixin):

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
                                     order_date=timezone.now(),
                                     freight=14.5,
                                     ship_name="Order test",
                                     ship_city="Bucharest",
                                     ship_address="Ghencea 1, Bucuresti",
                                     ship_country="Romania"
                                     )

    def test_create_order(self):
        customer = Customer.objects.get(pk='TEST1')
        employee = Employee.objects.get(pk=1001)
        shipper = Shipper.objects.get(pk=101)
        order = Order(customer=customer,
                      employee=employee,
                      ship_via=shipper,
                      order_date=datetime.now(),
                      freight=14.5,
                      ship_name="Order test",
                      ship_city="Bucharest",
                      ship_address="Ghencea 1, Bucuresti",
                      ship_country="Romania"
                      )

        products = load_from_api_json(PRODUCTS_SERVICE_URL, None, product_list_result_handler)
        product_id1 = products[0].id
        sufficient_stock = load_from_api_json(PRODUCTS_SERVICE_URL + str(product_id1) + "/", None, check_stock,
                                              {'quantity': 5})
        self.assertTrue(sufficient_stock)
        product_id2 = products[1].id
        sufficient_stock = load_from_api_json(PRODUCTS_SERVICE_URL + str(product_id2) + "/", None, check_stock,
                                              {'quantity': 7})
        self.assertTrue(sufficient_stock)
        order_detail1 = OrderDetail(product_id=products[0].id, quantity=5, order=order, unit_price=10)
        order_detail2 = OrderDetail(product_id=products[1].id, quantity=7, order=order, unit_price=2)
        order.save()
        self.logger.debug(order_detail1)
        order_detail1.save()
        self.logger.debug(order_detail2)
        order_detail2.save()
        stock_update = {"units_in_stock": 5}
        status_code = update(PRODUCTS_SERVICE_URL + str(product_id1) + "/", json.dumps(stock_update))
        self.assertTrue(status_code < 400)
        stock_update = {"units_in_stock": 7}
        status_code = update(PRODUCTS_SERVICE_URL + str(product_id2) + "/", json.dumps(stock_update))
        self.assertTrue(status_code < 400)
