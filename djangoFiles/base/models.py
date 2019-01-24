"""Base models that are going to be used everywhere."""

import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class AbstractUserModel(models.Model):

    class Meta:
        abstract = True

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


class AbstractTimeModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=timezone.now)


class AbstractUUIDModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)


class AbstractBaseModel(
    AbstractUserModel, AbstractTimeModel, AbstractUUIDModel):

    class Meta:
        abstract = True
        ordering = ('-created_at',)
