from django.conf.urls import url

from oldrepo.views import UseOldRepo

app_name = 'oldrepo'

urlpatterns = [
    url(r'^oldrepo/(?P<repo_name>[\w\-]+)/$', UseOldRepo.as_view(), name='old-repo')
]
