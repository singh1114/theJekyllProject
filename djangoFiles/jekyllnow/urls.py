from django.conf.urls import url

from jekyllnow.views import (
    JekyllNowTheme
)

urlpatterns = [
    url(r'^jn-init/$', JekyllNowTheme.as_view(), name='jn-init'),
]
