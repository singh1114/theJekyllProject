"""Base models that are going to be used everywhere."""

from django.db import models

from base.choices import (
    QuantityType,
    ProductType
)


class Product(models.Model):
    """The base item model containing fields for every item."""

    product_type = models.CharField(
        max_length=200,
        choices=ProductType.choices,
        default=ProductType.VEGETABLE
    )
    quantity_type = models.CharField(
        max_length=200,
        choices=QuantityType.choices,
        default=QuantityType.KILOGRAM
    )
