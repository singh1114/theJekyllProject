from django.conf.urls import url, include

from startbootstrap.views import (
    SBSDataView
)
urlpatterns = [
    url(r'^sbs-site-data/$', SBSDataView.as_view(), name='sbs-site-data'),
]