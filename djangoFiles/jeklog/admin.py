from django.contrib import admin

from theJekyllProject.models import (
    CName,
    Page,
    Post,
    PostCategory,
    Repo,
    SiteData,
    SiteSocialProfile,
    SiteTheme
)


class PostAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'author', 'date', 'time', 'title',)
    list_display = ('repo', 'author', 'comments', 'date', 'time', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)


class SiteDataAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'name')
    list_display = ('repo', 'name', 'description')


admin.site.register(SiteData, SiteDataAdmin)
admin.site.register(SiteTheme)


class SocialProfileAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'email', 'facebook', 'github', 'twitter')
    list_display = ('repo', 'email', 'facebook', 'github', 'twitter')


admin.site.register(SiteSocialProfile, SocialProfileAdmin)


class PageAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'title', 'permalink')
    list_display = ('repo', 'title', 'permalink')


admin.site.register(Page, PageAdmin)


class RepoAdmin(admin.ModelAdmin):
    search_fields = ('repo', 'user')
    list_display = ('repo', 'main', 'user', 'template')


admin.site.register(Repo, RepoAdmin)


class CNameAdmin(admin.ModelAdmin):
    search_fields = ('c_name', 'repo',)
    list_display = ('repo', 'c_name',)


admin.site.register(CName, CNameAdmin)
