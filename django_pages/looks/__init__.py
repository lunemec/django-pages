# -*- encoding: utf-8 -*-

from django.core.cache import get_cache

from .models import Template


def get_template():
    """
    Returns current active template
    If there is none user-defined template, return 'default'

    @return string
    """

    try:

        cache = get_cache('default')

        if not cache.get('template'):

            current_template = Template.objects.get(active=True).template
            cache.set('template', current_template, 30)

        else:

            current_template = cache.get('template')

    except Template.DoesNotExist:

        current_template = 'default'

    return current_template
