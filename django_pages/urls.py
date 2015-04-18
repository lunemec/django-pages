# -*- encoding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

from filebrowser.sites import site

from .feed.feed import RssLatestPostsFeed, AtomLatestPostsFeed


urlpatterns = patterns(
    '',
    # filebrowser
    url(r'^admin/filebrowser/', include(site.urls)),

    # helper site (wizzard)
    url(r'^wizzard/$', TemplateView.as_view(template_name='wizzard.html')),

    # rss and atom feed
    url(r'^rss/', RssLatestPostsFeed()),
    url(r'^atom/', AtomLatestPostsFeed()),

    # robots.txt
    url(r'^robots.txt$', 'django_pages.views.robots'),
    # sitemap generator
    url(r'^sitemap.xml$', 'django_pages.views.generate_sitemap'),
    # django_pages url resolver
    url(r'^(?P<url>.*)$', 'django_pages.views.main_view'),
)
