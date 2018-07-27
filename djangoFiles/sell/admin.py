# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import arrow

from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe

from sell.models import (
    Customer,
    SellProduct
)

@admin.register(SellProduct)
class SellProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'get_product_type', 'get_quantity_type',
                    'get_item_name', 'quantity', 'get_cost_price',
                    'sell_time')
    list_editable = ('quantity',)
    list_display_links = ('item',)

    def get_product_type(self, purchase_product):
        return purchase_product.item.product_type

    def get_item_name(self, purchase_product):
        return purchase_product.item.item_name

    def get_cost_price(self, purchase_product):
        return purchase_product.item.cost_price

    def get_quantity_type(self, purchase_product):
        return purchase_product.item.quantity_type


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'email', 'take_order',
                    'today_order_amount', 'details')
    list_editable = ('mobile_number', 'email')
    list_display_links = ('name',)
    readonly_fields = ('take_order',)
    search_fields = ('name', 'email', 'mobile_number')

    def take_order(self, customer):
        return mark_safe(
            '<a href="/sell/customer/{}/add_item">Take order</a>'.format(
                customer.pk))

    def details(self, customer):
        return mark_safe(
            '<a href="/sell/customer/{}/details">See details</a>'.format(
                customer.pk))

    def today_order_amount(self, customer):
        sell_products = SellProduct.objects.filter(
            customer=customer, sell_time__date=arrow.utcnow().date())
        return sum([sell_product.price for sell_product in sell_products])
