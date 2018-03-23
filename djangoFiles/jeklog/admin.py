from django.contrib import admin

from theJekyllProject.models import CName
from theJekyllProject.models import Post
from theJekyllProject.models import PostCategory
from theJekyllProject.models import SiteData
from theJekyllProject.models import SiteTheme
from theJekyllProject.models import Page
from theJekyllProject.models import Repo


class PostAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'author', 'date', 'time', 'title',)
    list_display = ('repo', 'author', 'comments', 'date', 'time', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)


class SiteDataAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'title')
    list_display = ('repo', 'title', 'description')


admin.site.register(SiteData, SiteDataAdmin)
admin.site.register(SiteTheme)


class PageAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'title', 'permalink')
    list_display = ('repo', 'title', 'permalink')


admin.site.register(Page, PageAdmin)


class RepoAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'user')
    list_display = ('repo', 'main', 'user')


admin.site.register(Repo, RepoAdmin)


class CNameAdmin(admin.ModelAdmin):
    search_fields = ('c_name', 'repo',)
    list_display = ('repo', 'c_name',)


admin.site.register(CName, CNameAdmin)
