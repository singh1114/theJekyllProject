from django.conf.urls import url

from startbootstrap.views import (
    SBSPostView,
    SBSSiteDataView,
    SBSSocialDataView,
    SBSThemeView
)

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    url(r'^sbs-init/$', SBSThemeView.as_view(), name='sbs-init'),
    url(r'^sbs-site-data/$', SBSSiteDataView.as_view(), name='sbs-site-data'),
    url(r'^sbs-social-data/$', SBSSocialDataView.as_view(),
        name='sbs-social-data'),
    url(r'^sbs-post/$', SBSPostView.as_view(), name='sbs-post'),
    url(r'^sbs-post/(?P<pk>\d+)/$', SBSPostView.as_view(), name='post-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
