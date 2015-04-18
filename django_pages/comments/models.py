# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..pages.models import Post


class Comment(models.Model):
    """
    Stores comment data.
    Is related to :model: `pages.Post`.
    """
    post = models.ForeignKey(Post)
    user = models.CharField(_('User'), max_length=100)
    comment = models.TextField(_('Comment'), max_length=1000)
    ip = models.CharField(_('IP'), max_length=100, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.user, self.comment[:50])

    class Meta:
        app_label = 'django_pages'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
