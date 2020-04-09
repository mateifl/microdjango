from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from app.api import CustomerResource, OrderResource
from app.views import CreateOrderView, DisplayOrderView, OrderErrorView
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(CustomerResource())
v1_api.register(OrderResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    path('create_order/', CreateOrderView.as_view(), name="create_order"),
    path('display_order/<order_id>/', DisplayOrderView.as_view(), name="display_order"),
    path('error_order/', OrderErrorView.as_view(), name="error_order")
]
