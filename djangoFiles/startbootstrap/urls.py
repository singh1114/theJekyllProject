from django.conf.urls import url

from startbootstrap.views import (
    SBSSiteDataView,
    SBSSocialDataView
)
urlpatterns = [
    url(r'^sbs-site-data/$', SBSSiteDataView.as_view(), name='sbs-site-data'),
    url(r'^sbs-social-data/$', SBSSocialDataView.as_view(),
        name='sbs-social-data'),
]
