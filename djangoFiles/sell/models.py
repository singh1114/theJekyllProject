# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from gcproduct.models import Item


class SellProduct(models.Model):
    """Every sold product information is stored."""
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE)
    mobile_number = models.CharField(
        max_length=10, null=True, blank=True)
    email = models.EmailField(
        max_length=300, null=True, blank=True)
    quantity = models.DecimalField(
        decimal_places=2, max_digits=10)
    price_paid = models.DecimalField(
        decimal_places=2, max_digits=10)
    sell_time = models.DateTimeField(
        auto_now_add=True)
