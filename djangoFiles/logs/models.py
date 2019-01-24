# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from base.models import AbstractBaseModel


class AccessLog(AbstractBaseModel):

    response_time = models.IntegerField()
    path = models.CharField(max_length=400, blank=True, null=True)
    method = models.CharField(max_length=200, blank=True, null=True)
    request_data = models.CharField(max_length=5000)
    response_data = models.CharField(max_length=5000)
    status_code = models.IntegerField()
    ip = models.CharField(max_length=100, blank=True, null=True)
    user_agent = models.CharField(max_length=100, blank=True, null=True)
