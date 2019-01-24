# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from logs.models import AccessLog


@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):

    list_display = (
        'uuid', 'created_by', 'created_at', 'response_time', 'path', 'method',
        'request_data', 'response_data', 'status_code', 'ip', 'user_agent')

    search_fields = (
        'user__username', 'uuid', 'ip', 'user_agent')
