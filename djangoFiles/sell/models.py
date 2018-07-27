# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from gcproduct.models import Item


class Customer(models.Model):
    """Customer database that can store the data of customers."""
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(
        max_length=10, null=True, blank=True)
    email = models.EmailField(
        max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class SellProduct(models.Model):
    """Every sold product information is stored."""
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.DecimalField(
        decimal_places=2, max_digits=10)
    sell_time = models.DateTimeField(
        auto_now_add=True)

    @property
    def price(self):
        cost_price = self.item.cost_price
        profit = cost_price * self.item.profit_percent / 100
        return int(round((cost_price + profit) * self.quantity))

    def __str__(self):
        return self.item.item_name
