# -*- encoding: utf-8 -*-

import datetime

from django.db import models

from django.utils.text import slugify
from django.utils.timezone import make_aware, get_current_timezone
from django.utils.translation import ugettext_lazy as _

from ..menu.models import MenuItem
from ..metadata.models import MetaSet


class Page(models.Model):
    '''
    Stores page data.
    Please be careful with comments, and don't put them on the Page and also.
    to all the Posts on that Page.
    Is related to :model: `django_pages.MenuItem`.
    '''

    link = models.OneToOneField(MenuItem, verbose_name=_('Link'))
    title = models.CharField(_('Page title'), max_length=500)
    content = models.TextField(_('Page content'), blank=True)

    metadata_set = models.ForeignKey(MetaSet, verbose_name=('Meta set'), null=True, blank=True)

    active = models.BooleanField(_('Active'), blank=True, default=True)
    index = models.BooleanField(
        _('Index page'),
        help_text=_('This page will be landing page for language specified for link (menu item)'),
        blank=True
    )

    def __unicode__(self):

        return self.title

    def have_posts(self):
        """
        checks if Page has any Posts

        @return bool
        """

        if self.post_set.count():

            return True

        return False

    def get_url(self):
        """
        returns url for this page

        @return string
        """

        url_scheme = '/{country_code}/{link_url}'

        result = url_scheme.format(country_code=self.link.lang.country_code, link_url=self.link.url)

        return result

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')


class Post(models.Model):
    '''
    Stores post data.
    Posts are ment to be small paragraphs of text, sorted by date of creation.
    from newer (up) to older (down).
    Is related to :model: `django_pages.Page`.
    '''

    page = models.ForeignKey(Page, verbose_name=_('Page'))
    title = models.CharField(_('Post title'), max_length=200, unique=True)
    content = models.TextField(_('Post content'))
    comments = models.BooleanField(_('Enable comments'), blank=True)

    active = models.BooleanField(_('Active'), blank=True, default=True)

    visible_from = models.DateTimeField(
        _('Visible from'),
        help_text=_('Post will not be visible outside of specified date and time'),
        blank=True,
        null=True
    )
    visible_to = models.DateTimeField(
        _('Visible to'),
        help_text=_('Post will not be visible outside of specified date and time'),
        blank=True,
        null=True
    )

    created = models.DateTimeField(_('Date of creation'), blank=True, null=True)

    def __unicode__(self):

        return self.title

    def save(self, *args, **kwargs):

        if not self.created:

            self.created = make_aware(datetime.datetime.now(), get_current_timezone())

        super(Post, self).save(*args, **kwargs)

    def is_visible(self, now):
        """
        checks if the Post should be displayed or not

        @return bool
        """

        now = make_aware(now, get_current_timezone())

        if self.visible_from:

            if self.visible_from <= now:

                second_from = True

            else:

                second_from = False

        else:

            second_from = True

        if self.visible_to:

            if self.visible_to >= now:

                second_to = True

            else:

                second_to = False

        else:

            second_to = True

        if second_from and second_to:

            return True

        else:

            return False

    def get_url(self):
        """
        creates url for Post

        @return string
        """

        url_scheme = '/{country_code}/{link_url}/~{post_title}'

        title = slugify(self.title)

        result = url_scheme.format(country_code=self.page.link.lang.country_code, link_url=self.page.link.url, post_title=title)

        return result

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
