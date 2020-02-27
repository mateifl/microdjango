from app.logging import LoggerMixin

logger = LoggerMixin()


class Product:
    def __init__(self, id, name, units_in_stock, unit_price):
        self.id = id
        self.name = name
        self.units_in_stock = units_in_stock
        self.unit_price = unit_price


def product_result_handler(products):
    result = list()
    products_list = products['objects']
    for product_dict in products_list:
        product = Product(product_dict['productid'],
                          product_dict['product_name'],
                          product_dict['units_in_stock'],
                          product_dict['unit_price'])
        result.append(product)
    return result


def check_stock(product, params):
    logger.logger.debug(product)
    units_in_stock = product['units_in_stock']
    product_id = product['productid']
    logger.logger.debug("Check stock product %s stock %s" % (product_id, units_in_stock))
    if int(units_in_stock) < params['quantity']:
        return False
    else:
        return True
