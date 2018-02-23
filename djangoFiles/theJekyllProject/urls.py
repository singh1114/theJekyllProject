from django.conf.urls import url, include
from django.views.generic import TemplateView

from theJekyllProject.views import (
    AddPageView,
    AddPostView,
    BlogView,
    ChooseSiteView,
    CNameView,
    CreateRepoView,
    DecideHomeView,
    IndexView,
    PageListView,
    PageUpdateView,
    PostListView,
    PostUpdateView,
    RepoListView,
    SiteExcludeView,
    SelectMainSiteView,
    SitePluginView,
    SiteProfileView,
    SiteSocialProfileView,
    SiteThemeView
)

urlpatterns = [
    url(r'^registration/?', TemplateView.as_view(
        template_name='theJekyllProject/registration.html'),
        name='registration'),
    url(r'^index/?', IndexView.as_view(), name='index'),
    url(r'^$', DecideHomeView.as_view(), name='decide-home-view'),
    url(r'^repolist/?', RepoListView.as_view(), name='repo-list'),
    url(r'^createrepo/?', CreateRepoView.as_view(), name='create-repo'),

    url(r'^choosesite/?', ChooseSiteView.as_view(), name='choose-site'),
    url(r'^selectmainsite/(?P<pk>\d+)$', SelectMainSiteView.as_view(),
        name='select-main-site'),

    url(r'^addpost/?', AddPostView.as_view(), name='addpost'),
    url(r'^updatepost/(?P<pk>\d+)$', PostUpdateView.as_view(),
        name='post-update'),

    url(r'^siteprofile/?', SiteProfileView.as_view(), name='siteprofile'),
    # url(r'^sitedataupdate/?', SiteDataUpdateView.as_view(),
    #    name='siteprofile'),
    url(r'^ckeditor/', include('froala_editor.urls')),
    url(r'^home/?', PostListView.as_view(), name='home'),
    url(r'^sitesocialprofile/?', SiteSocialProfileView.as_view(),
        name='socialprofile'),
    url(r'^siteplugin/?', SitePluginView.as_view(), name='siteplugin'),
    url(r'^siteexclude/?', SiteExcludeView.as_view(), name='siteexclude'),
    url(r'^sitetheme/?', SiteThemeView.as_view(), name='sitetheme'),

    # urls about pages
    url(r'^updatepage/(?P<pk>\d+)$', PageUpdateView.as_view(),
        name='page-update'),
    url(r'^addpage/?', AddPageView.as_view(), name='add-page'),
    url(r'^pages/?$', PageListView.as_view(), name='page-list'),

    # Blog view
    url(r'^yourblog/?', BlogView.as_view(), name='your-blog'),

    # Cname
    url(r'^cname/?', CNameView.as_view(), name='cname')
]
