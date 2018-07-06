# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from gcproduct.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'quantity_type', 'item_name',
                    'profit_percent', 'cost_price')
    list_editable = ('item_name', 'profit_percent', 'cost_price')
    list_display_links = ('product_type',)
