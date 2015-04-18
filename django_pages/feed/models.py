# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class FeedSettings(models.Model):
    """
    Stores Rss/Atom feed settings
    """
    active = models.BooleanField(_('Feed enabled'), default=True)
    site_title = models.CharField(
        _('Title'),
        help_text=_('Feed title for entire site'),
        max_length=200
    )
    site_description = models.TextField(
        _('Description'),
        help_text=_('Feed description for entire site'),
        max_length=1000
    )
    latest_post_count = models.IntegerField(
        _('Post count'),
        help_text=_('How many latest Post to be displayed'),
        default=10
    )

    class Meta():
        app_label = 'django_pages'
        verbose_name = _('Feed Settings')
        verbose_name_plural = _('Feed Settings')

    def __unicode__(self):
        return self.site_title
