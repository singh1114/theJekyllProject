from django.conf.urls import url

from oldrepo.views import UseOldRepo

urlpatterns = [
    url(r'^oldrepo/?', UseOldRepo.as_view(), name='old-repo')
]
