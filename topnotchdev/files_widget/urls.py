try:
    from django.conf.urls import url, include
except:
    from django.conf.urls import patterns, url
from topnotchdev.files_widget.views import upload, thumbnail_url

# from django.conf import settings

urlpatterns = [
    url(r'^upload/$', upload, name="files_widget_upload"),
    url(r'^thumbnail-url/$', thumbnail_url, name="files_widget_get_thumbnail_url"),
]
