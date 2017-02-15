# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from topnotchdev.files_widget.urls import urlpatterns as files_widget_urls

urlpatterns = [
    url(r'^', include(files_widget_urls, namespace='files-widget')),
]
