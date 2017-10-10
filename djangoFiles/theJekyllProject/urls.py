from django.conf.urls import url, include

from theJekyllProject.views import AddPostView
from theJekyllProject.views import SiteProfileView
from theJekyllProject.views import SiteSocialProfileView
from theJekyllProject.views import SitePluginView
from theJekyllProject.views import SiteExcludeView
from theJekyllProject.views import SiteThemeView
from theJekyllProject.views import PostListView
from theJekyllProject.views import PostUpdateView
from theJekyllProject.views import RepoListView
from theJekyllProject.views import CreateRepoView

urlpatterns = [
    url(r'^repolist/?', RepoListView.as_view(), name='repo-list'),
    url(r'^createrepo/?', CreateRepoView.as_view(), name='create-repo'),
    
    url(r'^addpost/?', AddPostView.as_view(), name='addpost'),
    url(r'^updatepost/(?P<pk>\d+)$', PostUpdateView.as_view(), name='post-update'),

    url(r'^siteprofile/?', SiteProfileView.as_view(), name='siteprofile'),
#    url(r'^sitedataupdate/?', SiteDataUpdateView.as_view(), name='siteprofile'),
    url(r'^ckeditor/', include('froala_editor.urls')),
    url(r'^home/?', PostListView.as_view(), name='home'),
    url(r'^sitesocialprofile/?', SiteSocialProfileView.as_view(), name='socialprofile'),
    url(r'^siteplugin/?', SitePluginView.as_view(), name='siteplugin'),
    url(r'^siteexclude/?', SiteExcludeView.as_view(), name='siteexclude'),
    url(r'^sitetheme/?', SiteThemeView.as_view(), name='sitetheme'),
]
