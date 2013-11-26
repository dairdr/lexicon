# -*- encoding: utf-8 -*-
"""Common urls config."""
from django.contrib import admin
from django.conf.urls import patterns, include, url
from lexicon.apps.dictionary import urls as dictionary_urls
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()

urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^backdoor/admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^backdoor/admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
	# Local apps
	url(r'^dictionary/', include(dictionary_urls, namespace='dictionary')),
)