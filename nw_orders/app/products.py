

class Product:
    def __init__(self, id, name, units_in_stock, unit_price, units_on_order):
        self.id = id
        self.name = name
        self.units_in_stock = units_in_stock
        self.unit_price = unit_price
        self.units_on_order = units_on_order


def product_list_result_handler(products):
    result = list()
    products_list = products['objects']
    for product_dict in products_list:
        product = Product(product_dict['productid'],
                          product_dict['product_name'],
                          product_dict['units_in_stock'],
                          product_dict['unit_price'],
                          product_dict['units_on_order'])
        result.append(product)
    return result


def product_result_handler(payload):
    product = Product(payload['productid'],
                      payload['product_name'],
                      payload['units_in_stock'],
                      payload['unit_price'],
                      payload['units_on_order'])
    return product
