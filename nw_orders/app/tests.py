from django.test import TestCase
from app.rest_client import update
from app.config import PRODUCTS_SERVICE_URL

class OrdersTests(TestCase):
    def test_update_stock(self):
        update_url = PRODUCTS_SERVICE_URL + "2/"
        update_body = {"units_in_order": 23, "units_is_stock": 10}
        status_code = update(update_url, update_body)
        self.assertTrue(status_code < 400)
