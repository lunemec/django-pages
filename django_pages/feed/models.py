# -*- encoding: utf-8 -*-

from django.db import models


class FeedSettings(models.Model):
    '''
    Stores Rss/Atom feed settings
    '''

    active = models.BooleanField('Feed enabled', default=True)
    site_title = models.CharField('Site Feed title', max_length=200)
    site_description = models.TextField('Site Feed description', max_length=1000)
    latest_post_count = models.IntegerField('Latest Post count to show', default=10)

    class Meta():

        verbose_name_plural = 'Feed Settings'

    def __unicode__(self):

        return self.site_title


