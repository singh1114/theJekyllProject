# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from purchase.models import PurchaseProduct


@admin.register(PurchaseProduct)
class PurchaseProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'get_product_type', 'get_quantity_type',
                    'get_item_name', 'quantity', 'get_cost_price')
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
