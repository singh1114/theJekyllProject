from django.conf.urls import url, include

from theJekyllProject.views import AddPostView
from theJekyllProject.views import home
urlpatterns = [
    url(r'^addpost/?', AddPostView.as_view(), name='addpost'),
    url(r'^ckeditor/', include('froala_editor.urls')),
    url(r'^home/?', home, name='home')
]
