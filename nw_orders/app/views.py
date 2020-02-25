from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from app.rest_client import load_from_api_json
from app.products import product_result_handler
from app.models import Customer, Employee, Shipper, Order, OrderDetail
from app.forms import CreateOrderForm
from datetime import datetime
from app.config import PRODUCTS_SERVICE_URL


def check_string_has_value(s):
    if s is None or len(s) == 0:
        return False
    return True


def check_string_has_value_dict(d, key):
    if key in d and check_string_has_value(d[key]):
        return d[key]
    return None


class CreateOrderView(FormView):
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
        print("CreateOrderView.post")
        # print(request.kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            print('form valid')
            return self.form_valid(form, **kwargs)
        else:
            print("form invalid")
            print(form.errors)
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        print("CreateOrderView.form_valid")
        customer_id = check_string_has_value_dict(form.cleaned_data, "customer")
        employee_id = check_string_has_value_dict(form.cleaned_data, "employee")
        shipper_id = check_string_has_value_dict(form.cleaned_data, "shipper")
        customer = Customer.objects.get(pk=customer_id)
        employee = Employee.objects.get(pk=employee_id)
        shipper = Shipper.objects.get(pk=shipper_id)
        now = datetime.now()
        order = Order(customer = customer, employee = employee, ship_via = shipper, order_date = now)
        order.save()
        product = check_string_has_value_dict(form.cleaned_data, "product")
        quantity = check_string_has_value_dict(form.cleaned_data, "quantity")

        order_detail = OrderDetail(product_id = product, quantity = quantity, order = order)
        order_detail.save()

        # self.success_url = reverse('order_view', args=[order_id])
        return super(CreateOrderView, self).form_valid(form)


    class DisplayOrderView(TemplateView):

        template_name = "order_create.html"
