"""Choices for base class."""

from djchoices import (
    DjangoChoices,
    ChoiceItem
)


class ProductType(DjangoChoices):
    VEGETABLE = ChoiceItem('VEGETABLE')
    FRUIT = ChoiceItem('FRUIT')


class QuantityType(DjangoChoices):
    DOZEN = ChoiceItem('DOZEN')
    KILOGRAM = ChoiceItem('KILOGRAM')
