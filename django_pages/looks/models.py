# -*- encoding: utf-8 -*-

from django.db import models


class Template(models.Model):
    '''
    Stores template information.
    Template name is used for template selection in templates foled of your project
    '''

    template = models.CharField('Template name', max_length=200)
    posts_per_page = models.PositiveIntegerField('Posts per page', default=10)
    active = models.BooleanField('Active', default=False, blank=True)

    def __unicode__(self):

        return self.template
