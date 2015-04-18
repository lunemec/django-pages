# -*- encoding: utf-8 -*-

from django.core.cache import caches

from .models import Template


def get_template():
    """
    Returns current active template
    If there is none user-defined template, return 'default'

    @return (string, int)
    """
    try:
        cache = caches['default']

        if not cache.get('template'):
            template = Template.objects.get(active=True)
            current_template = (template.template, template.submenu_max_characters)
            cache.set('template', current_template, 30)

        else:
            current_template = cache.get('template')

    except Template.DoesNotExist:
        current_template = ('default', 150)

    return current_template
