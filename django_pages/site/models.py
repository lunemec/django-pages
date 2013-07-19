# -*- encoding: utf-8 -*-

from django.db import models


class Site(models.Model):

    domain = models.CharField('Domain', max_length=150)
    display_name = models.CharField('Display name', max_length=200)
    tagline = models.CharField('Tagline', max_length=200, blank=True)
    footer = models.TextField('Footer', max_length=1000, blank=True)

    def __unicode__(self):

        return self.domain
