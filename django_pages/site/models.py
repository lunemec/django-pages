# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Site(models.Model):
    """
    Model for site settings
    there is supposed to by only one Site
    (for now)
    """
    domain = models.CharField(_('Domain'), max_length=150)
    display_name = models.CharField(_('Website name'), max_length=200)
    tagline = models.CharField(
        _('Tagline'),
        help_text=_('Smaller text next to website name'),
        max_length=200,
        blank=True
    )
    footer = models.TextField(
        _('Footer'),
        help_text=_('Custom footer with HTML to be displayed on each page'),
        max_length=1000,
        blank=True
    )

    def __unicode__(self):
        return self.domain

    class Meta:
        app_label = 'django_pages'
        verbose_name = _('Site')
        verbose_name_plural = _('Sites')


class Script(models.Model):
    """
    Model for scripts that should
    be inserted on each page (like footer above)

    for example google analytics/facebook/google+ ..
    """
    name = models.CharField(
        _('Name'),
        help_text=_('Script identification'),
        max_length=50
    )
    code = models.TextField(
        _('Code'),
        help_text=_('Source code for script to be inserted, including &lt;script&gt;&lt;/script&gt; tags'),
        max_length=1000
    )

    class Meta:
        app_label = 'django_pages'
        verbose_name = _('Script')
        verbose_name_plural = _('Scripts')
