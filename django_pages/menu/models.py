# -*- encoding: utf-8 -*-

from django.db import models

from ..language.models import Language


class MenuItem(models.Model):
    '''
    Stores menuitem information.
    It is recommended to write urls in SEO format, e.g.: this_is_my_site_describing_something.
    Is related to :model: `django_pages.Menu`.
    '''

    lang = models.ForeignKey(Language)
    menuitem_name = models.CharField('MenuItem name', max_length=200)
    url = models.SlugField('Url', max_length=200, unique=True)
    position = models.IntegerField('Position', blank=True)

    def __unicode__(self):

        return '%s - %s' % (self.menuitem_name, self.lang)

    def save(self, *args, **kwargs):
        """
        if MenuItem does not contain position, set it to last_item's_position + 1
        """

        if not self.position:

            last_position = self.get_last_position()

            self.position = last_position + 1

        super(MenuItem, self).save(*args, **kwargs)

    def get_last_position(self):
        """
        returns last_item's_position or 0 (no items)
        """

        other_objects = MenuItem.objects.filter(lang=self.lang).order_by('-position')

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

        object_to_swap_with = MenuItem.objects.get(lang=self.lang, position=position)

        object_to_swap_with.position = self.position
        object_to_swap_with.save()

        self.position = position
        self.save()

    def is_current(self, page_url):
        """
        checks if this is currently active menuitem

        @return bool
        """

        if page_url == self.url or (self.page.index and self.page.active and page_url is None):

            return True

        return False
