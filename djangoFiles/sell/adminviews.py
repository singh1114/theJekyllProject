import arrow

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from gcproduct.models import Item

from sell.models import Customer, SellProduct
from sell.forms import SellProductForm


class SellProductAdminView(View):
    def get(self, request, customer_pk, *args, **kwargs):
        customer = Customer.objects.get(pk=customer_pk)
        return render(request, 'sell/sell_product.html', {
            'form': SellProductForm,
            'customer_name': customer.name
        })

    def post(self, request, customer_pk, *args, **kwargs):
        customer = Customer.objects.get(pk=customer_pk)
        request_data = request.POST.dict()
        quantity = request_data['quantity']
        item_pk = request_data['item']
        item = Item.objects.get(pk=item_pk)
        SellProduct.objects.create(
            item=item, customer=customer, quantity=quantity)
        return HttpResponseRedirect(reverse('admin:sell_customer_changelist'))


class CustomerOrderAdminView(View):
    def get(self, request, customer_pk, *args, **kwargs):
        customer = Customer.objects.get(pk=customer_pk)
        sell_products = SellProduct.objects.filter(
            customer=customer, sell_time__date=arrow.utcnow().date())
        return render(request, 'sell/customer_order_details.html', {
            'customer_name': customer.name,
            'customer_email': customer.email,
            'customer_mobile_number': customer.mobile_number,
            'sell_products': sell_products
        })
