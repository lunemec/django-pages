# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Template(models.Model):
    """
    Stores template information.
    Template name is used for template selection in templates foled of your project
    """
    template = models.CharField(_('Template name'), max_length=200)
    submenu_max_characters = models.PositiveIntegerField(_('Max characters in submenu'), default=150)
    active = models.BooleanField(_('Active'), default=False, blank=True)

    def __unicode__(self):
        return self.template

    def save(self, *args, **kwargs):
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

    class Meta:
        app_label = 'django_pages'
        verbose_name = _('Template')
        verbose_name_plural = _('Templates')
