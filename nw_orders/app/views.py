from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse
from app.rest_client import load_from_api_json, update
from app.products import product_result_handler, check_stock
from app.models import Customer, Employee, Shipper, Order, OrderDetail
from app.forms import CreateOrderForm
from django.utils import timezone
from app.config import PRODUCTS_SERVICE_URL
from app.logging import LoggerMixin


def check_string_has_value(s):
    if s is None or len(s) == 0:
        return False
    return True


def check_string_has_value_dict(d, key):
    if key in d and check_string_has_value(d[key]):
        return d[key]
    return None


class CreateOrderView(FormView, LoggerMixin):
    template_name = "order_create.html"
    form_class = CreateOrderForm

    def get_context_data(self, **kwargs):
        # load the products from the product app using REST call
        products = load_from_api_json(PRODUCTS_SERVICE_URL, None, product_result_handler)
        customers = Customer.objects.all()
        employees = Employee.objects.all()
        shippers = Shipper.objects.all()
        context = super(CreateOrderView, self).get_context_data(**kwargs)
        if len(products) > 0:
            context['products'] = products
        context['customers'] = customers
        context['employees'] = employees
        context['shippers'] = shippers
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            self.logger.error("form invalid")
            self.logger.error(form.errors)
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        customer_id = check_string_has_value_dict(form.cleaned_data, "customer")
        employee_id = check_string_has_value_dict(form.cleaned_data, "employee")
        shipper_id = check_string_has_value_dict(form.cleaned_data, "shipper")
        freight = form.cleaned_data["freight"]
        ship_name = check_string_has_value_dict(form.cleaned_data, "ship_name")
        ship_country = check_string_has_value_dict(form.cleaned_data, "ship_country")
        ship_city = check_string_has_value_dict(form.cleaned_data, "ship_city")
        address = check_string_has_value_dict(form.cleaned_data, "address")

        self.logger.debug("loading customer id %s" % customer_id)
        customer = Customer.objects.get(pk=customer_id)
        self.logger.debug("loading employee id %d" % employee_id)
        employee = Employee.objects.get(pk=employee_id)
        self.logger.debug("loading shipper id %d" % shipper_id)
        shipper = Shipper.objects.get(pk=shipper_id)
        now = timezone.now()

        order = Order(customer=customer, employee=employee, ship_via=shipper, order_date=now,
                      freight=int(freight), ship_city=ship_city, ship_country=ship_country, ship_address=address)

        product = check_string_has_value_dict(form.cleaned_data, "product")
        product_id, unit_price, units_in_stock = product.split("|")
        product_id = int(product_id)
        unit_price = float(unit_price)
        units_in_stock = int(units_in_stock)
        quantity = check_string_has_value_dict(form.cleaned_data, "quantity")

        if quantity > units_in_stock:
            self.logger.info("Not enough stock")
            self.success_url = reverse('display_order', args=[-1])
            return super(CreateOrderView, self).form_valid(form)
        self.logger.info("updating stock")
        status_code = update(PRODUCTS_SERVICE_URL + "/" + str(product_id) + "/", {"units_in_stock": units_in_stock - quantity})
        if status_code >= 400:
            self.logger.error("Stock not updated!")
            raise Exception("stock not updated")
        self.logger.debug("saving order")
        order.save()
        order_detail = OrderDetail(product_id=product_id, quantity=quantity, order=order, unit_price=unit_price)
        order_detail.save()

        self.logger.debug("order saved")
        self.success_url = reverse('display_order', args=[order.orderid])
        return super(CreateOrderView, self).form_valid(form)


class DisplayOrderView(TemplateView):

    template_name = "order_display.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayOrderView, self).get_context_data(**kwargs)
        order_id = int(kwargs['order_id'])
        if order_id < 0:
            context['message'] = 'No order created'
        else:
            context['message'] = 'Order created, id = ' + str(order_id)
        return context
