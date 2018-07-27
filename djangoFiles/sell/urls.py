from django.conf.urls import url, include
from django.views.generic import TemplateView

from sell.adminviews import (
    CustomerOrderAdminView,
    SellProductAdminView,
)

urlpatterns = [
    url(r'^sell/customer/(?P<customer_pk>[0-9]+)/add_item/?', SellProductAdminView.as_view(),
        name='add_item'),
    url(r'^sell/customer/(?P<customer_pk>[0-9]+)/details/?',
        CustomerOrderAdminView.as_view(),
        name='order_details'),
]
