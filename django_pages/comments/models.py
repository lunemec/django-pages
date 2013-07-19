# -*- encoding: utf-8 -*-

from django.db import models

from django_pages.pages.models import Post


class Comment(models.Model):
    '''
    Stores comment data.
    Is related to :model: `django_pages.Post`.
    '''

    post = models.ForeignKey(Post)
    user = models.CharField('User', max_length=100)
    comment = models.TextField('Comment', max_length=1000)
    ip = models.CharField('IP', max_length=100, blank=True)

    def __unicode__(self):

        return '%s@%s' % (self.user, self.comment[:50])
