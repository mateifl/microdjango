from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from app.rest_client import load_from_api_json
from app.products import product_result_handler
from app.models import Customer, Employee, Shipper, Order, OrderDetails
from app.forms import CreateOrderForm


def check_string_has_value(s):
    if s is None or len(s) == 0:
        return False
    return True


def check_string_has_value_dict(d, key):
    if key in d and check_string_has_value(d[key]):
        return d[key]
    return None


class CreateOrderView(TemplateView):
    template_name = "order_create.html"

    form_class = CreateOrderForm

    def get_context_data(self, **kwargs):
        # load the products from the product app using REST call
        products = load_from_api_json("http://127.0.0.1:8001/api/v1/product", None, product_result_handler)
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

    # def post(self, request, *args, **kwargs):
    #     self.logger.debug("CreateOrderView.post")
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     if form.is_valid():
    #         self.logger.debug('form valid')
    #         return self.form_valid(form, **kwargs)
    #     else:
    #         self.logger.error("Form is invalid")
    #         print(form.errors)
    #         return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        self.logger.debug("CreateOrderView.form_valid")
        product = check_string_has_value_dict(form.cleaned_data, "product")
        quantity = check_string_has_value_dict(form.cleaned_data, "quantity")
        order_detail = OrderDetails(product = product, quantity = quantity)
        order_detail.save()
        customer = check_string_has_value_dict(form.cleaned_data, "customer")
        employee = check_string_has_value_dict(form.cleaned_data, "employee")

        # self.success_url = reverse('order_view', args=[order_id])
        return super(CreateOrderView, self).form_valid(form)


    class DisplayOrderView(TemplateView):

        template_name = "order_create.html"
