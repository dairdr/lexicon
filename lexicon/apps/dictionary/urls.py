# -*- encoding: utf-8 -*-
"""Defines all urls conf."""
from django.conf.urls import patterns, url
from views import IndexView, ProjectView, ContactView, ThanksView, ResultView, ResultByIndexView, WordView

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name='dictionary-index'), # index web
	url(r'^contact/$', ContactView.as_view(), name='dictionary-contact'), # contact page
	url(r'^project/$', ProjectView.as_view(), name='dictionary-project'), # project page
	url(r'^search/$', ResultView.as_view(), name='dictionary-search'), # search a word
	url(r'^index/(?P<letter>\w{1})/$', ResultByIndexView.as_view(), name='dictionary-search-by-index'), # search by index
	url(r'^word/(?P<word>\d+)/$', WordView.as_view(), name='dictionary-word'), # view a info word
	url(r'^thanks/$', ThanksView.as_view(), name='dictionary-thanks'), # response to sent message
)