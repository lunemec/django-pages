# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..language.models import Language


class Menu(models.Model):
    """
    Stores data about menu.
    There may be reason to have multiple menu
    Links in the header for example
    """
    name = models.CharField(
        _('Menu name'),
        help_text=_('For identification only'),
        max_length=200
    )

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'django_pages'
        verbose_name = _('Menu')
        verbose_name_plural = _('Menu')


class MenuItem(models.Model):
    """
    Stores menuitem information.
    It is recommended to write urls in SEO format,
    e.g.: this_is_my_site_describing_something.
    Is related to :model: `django_pages.Menu`.
    """
    lang = models.ForeignKey(Language, verbose_name=_('Language'))
    menu = models.ForeignKey(Menu, verbose_name=_('Menu'))
    menuitem_name = models.CharField(_('Menu item name'), max_length=200)
    url = models.CharField(
        _('Url'),
        help_text=_('It is recommended to write urls in SEO format, '
                    'e.g.: this_is_my_site_describing_something.'),
        max_length=200
    )
    position = models.IntegerField(_('Position'), blank=True)
    style = models.CharField(
        _('Style'),
        help_text=_('Custom style for this menu item'),
        max_length=200,
        blank=True
    )

    def __unicode__(self):
        return '%s - %s' % (self.menuitem_name, self.lang)

    def save(self, *args, **kwargs):
        """
        if MenuItem does not contain position,
        set it to last_item's_position + 1
        """
        if not self.position:

            last_position = self.get_last_position()
            self.position = last_position + 1

        super(MenuItem, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        makes sure that there is no spaces in positioning after delete
        """
        super(MenuItem, self).delete(*args, **kwargs)
        self.reorder_items()

    def reorder_items(self):
        """
        repositions items after deletion or exception
        """
        items = MenuItem.objects.filter(
            lang=self.lang,
            menu=self.menu
        ).order_by('position')

        for pos, item in enumerate(items):
            item.position = pos + 1
            item.save()

    def get_last_position(self):
        """
        returns last_item's_position or 0 (no items)
        """
        other_objects = MenuItem.objects.filter(
            lang=self.lang,
            menu=self.menu
        ).order_by('-position')

        if other_objects.count():
            last_position = other_objects[0].position

        else:
            last_position = 0

        return last_position

    def is_first(self):
        """
        returns True if self.position is 1, False otherwise
        """
        if self.position == 1:
            return True

        return False

    def is_last(self):
        """
        if self.position is last, return True, False otherwise

        @return bool
        """
        last_position = self.get_last_position()

        if self.position == last_position:
            return True

        return False

    def increase_position(self):
        """
        moves this item to self.position + 1
        """
        if self.is_last():
            pass

        else:
            self.swap_with(self.position + 1)

    def decrease_position(self):
        """
        moves this item to self.position - 1
        """
        if self.is_first():
            pass

        else:
            self.swap_with(self.position - 1)

    def swap_with(self, position):
        """
        handles item moving, makes sure there are no items with same position
        """
        try:
            object_to_swap_with = MenuItem.objects.get(
                lang=self.lang,
                menu=self.menu,
                position=position
            )

            object_to_swap_with.position = self.position
            object_to_swap_with.save()

            self.position = position
            self.save()

        except MenuItem.DoesNotExist:
            self.reorder_items()

    def is_current(self, page_url):
        """
        checks if this is currently active menuitem

        @return bool
        """
        if page_url == self.url or (
            self.page.index and self.page.active and page_url is None
        ):

            return True

        return False

    def get_url(self):
        """
        returns url for django-page or http link
        if 'http://' is in self.url or 'https://'
        """
        if 'http://' in self.url or 'https://' in self.url:
            return self.url

        else:
            return '/{}/{}'.format(self.lang.country_code, self.url)

    class Meta:
        app_label = 'django_pages'
        verbose_name = _('Menu item')
        verbose_name_plural = _('Menu items')
