# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from theJekyllProject.models import CName
from theJekyllProject.models import Post
from theJekyllProject.models import PostCategory
from theJekyllProject.models import SiteData
from theJekyllProject.models import SiteTheme
from theJekyllProject.models import Page
from theJekyllProject.models import Repo
# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(SiteData)
admin.site.register(SiteTheme)
admin.site.register(Page)
admin.site.register(Repo)

class CNameAdmin(admin.ModelAdmin):
    search_fields = ('cname', 'repo',)
    list_display = ('repo', 'cname',)

admin.site.register(CName)
