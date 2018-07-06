# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from gcproduct.models import Item


class PurchaseProduct(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE)
    purchase_time = models.DateTimeField(
        auto_now_add=True)
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2)
