# -*- encoding: utf-8 -*-

from django.db import models


class Site(models.Model):
    """
    Model for site settings
    there is supposed to by only one Site
    (for now)
    """

    domain = models.CharField('Domain', max_length=150)
    display_name = models.CharField('Display name', max_length=200)
    tagline = models.CharField('Tagline', max_length=200, blank=True)
    footer = models.TextField('Footer', max_length=1000, blank=True)

    def __unicode__(self):

        return self.domain


class Script(models.Model):
    """
    Model for scripts that should
    be inserted on each page (like footer above)

    for example google analytics/facebook/google+ ..
    """

    name = models.CharField('Name', help_text='Script identification', max_length=50)
    code = models.TextField('Code', help_text='Source code for script to be inserted, including &lt;script&gt;&lt;/script&gt; tags', max_length=1000)
