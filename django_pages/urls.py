# -*- encoding: utf-8 -*-

"""
Default URL scheme for django-pages
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from django.views.generic import TemplateView

from .common.errors import ConfigurationError
from .feed.feed import RssLatestPostsFeed, AtomLatestPostsFeed
from .settings import ADMIN_URL


def get_admin_urls(ADMIN_URL):
    """
    Checks that admin url
    has required format

    @param ADMIN_URL: string
    @return tuple
    """

    # no / as a first character
    try:
        assert('/' not in ADMIN_URL[0])
    except AssertionError:
        raise ConfigurationError('ADMIN_URL has "/" at the beginning!')

    try:
        assert('/' in ADMIN_URL[-1])
    except AssertionError:
        raise ConfigurationError('ADMIN_URL does not have "/" at the end!')

    admindoc_url = r'^' + ADMIN_URL + 'doc/'
    admin_url = r'^' + ADMIN_URL

    return (admindoc_url, admin_url)


admin_urls = get_admin_urls(ADMIN_URL)

urlpatterns = patterns(
    '',

    # admin part
    url(admin_urls[0], include('django.contrib.admindocs.urls')),
    url(admin_urls[1], include(admin.site.urls)),

    # ckeditor image upload connector
    url(r'^connector/browser/$', 'django_pages.connector.views.browser'),
    url(r'^connector/uploader/$', 'django_pages.connector.views.uploader'),

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
