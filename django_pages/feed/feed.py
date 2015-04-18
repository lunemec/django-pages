# -*- encoding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from ..pages.models import Post
from .models import FeedSettings


class RssLatestPostsFeed(Feed):
    link = '/'

    try:
        settings = FeedSettings.objects.get(pk=1)

        if not settings.active:
            title = "Feeds are disabled for this site."
            description = ""
            post_count = 0

        else:
            title = settings.site_title
            description = settings.site_description
            post_count = int(settings.latest_post_count)

    except FeedSettings.DoesNotExist:
        title = "No FeedSettings found, create one in admin"
        description = "Please create exactly one feed setting in site administration"
        post_count = 5

    def items(self):
        return Post.objects.filter(active=True).order_by('-created')[:self.post_count]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return '{} ...'.format(item.content.encode('utf-8')[:200])

    def item_link(self, item):
        return item.get_url()


class AtomLatestPostsFeed(RssLatestPostsFeed):
    feed_type = Atom1Feed
