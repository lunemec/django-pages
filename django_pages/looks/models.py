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

    def save(self, *args, **kwargs):
        '''

        '''

        if not self.active:
            if not Template.objects.exists():
                self.active = True

        else:
            others = Template.objects.filter(active=True).exclude(id=self.id)

            for other_active in others:
                other_active.active = False
                super(Template, other_active).save(*args, **kwargs)

            self.active = True

        super(Template, self).save(*args, **kwargs)
