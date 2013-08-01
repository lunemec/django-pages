# -*- encoding: utf-8 -*-

from django.db import models

from ..language.models import Language


class MetaSet(models.Model):
    '''
    Stores MetaData configurations
    '''

    language = models.ForeignKey(Language)
    name = models.CharField('MetaSet name', max_length=200)

    def __unicode__(self):

        return self.name


class MetaData(models.Model):
    '''
    Stores MetaData item
    '''

    meta_set = models.ForeignKey(MetaSet)
    name = models.CharField('name', max_length=200)
    content = models.TextField('content')

    class Meta:

        verbose_name_plural = 'Meta data'

    def __unicode__(self):

        return '%s@%s' % (self.name, self.meta_set)


