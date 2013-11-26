# -*- encoding: utf-8 -*-
"""Development urls config."""
from common import *
from django.conf import settings
from django.conf.urls.static import static

# Serving uploaded files by user
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)