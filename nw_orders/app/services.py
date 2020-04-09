from app.rest_client import update, load_from_api_json
from app.products import product_result_handler
from app.config import PRODUCTS_SERVICE_URL
from app.logging import LoggerMixin

logger = LoggerMixin()

def check_and_update_stock(product_id, quantity):
    # load the stock to check if there are enough units 
    url = PRODUCTS_SERVICE_URL + str(product_id)
    product = load_from_api_json(url, None, product_result_handler)
    if product.units_in_stock < quantity:
        logger.logger.warn("Not enough products in stock")
        return False
    update_stock_body = {"units_in_stock": product.units_in_stock - quantity,
                         "units_on_order": product.units_on_order + quantity}
    status_code = update(url + "/", update_stock_body)
    if status_code >= 400:
        return False
    return True
