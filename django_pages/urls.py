from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from django.views.generic import TemplateView

from .feed.feed import RssLatestPostsFeed, AtomLatestPostsFeed

urlpatterns = patterns(
    '',
    # admin part
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

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
