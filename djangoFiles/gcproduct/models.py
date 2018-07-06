"""Models for green comestibles products."""

from __future__ import unicode_literals

from django.db import models

from base.models import Product


class Item(Product):
    """Items of GC."""
    item_name = models.CharField(max_length=200)
    profit_percent = models.IntegerField(default=5)
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name
