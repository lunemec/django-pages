# -*- encoding: utf-8 -*-

from django.db import models


class Log(models.Model):
    '''
    Stores request logs
    '''

    when = models.DateTimeField('When')
    logline = models.TextField('Log', max_length=10000)

    def __unicode__(self):

        return self.when.isoformat()
