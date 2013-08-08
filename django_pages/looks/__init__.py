# -*- encoding: utf-8 -*-

from django.core.cache import get_cache

from .models import Template


def get_template():
    """
    Returns current active template
    If there is none user-defined template, return 'default'

    @return (string, int)
    """

    try:

        cache = get_cache('default')

        if not cache.get('template'):

            template = Template.objects.get(active=True)
            template_name = template.template
            posts_count = template.posts_per_page

            current_template = (template_name, posts_count)
            cache.set('template', current_template, 30)

        else:

            current_template = cache.get('template')

    except Template.DoesNotExist:

        current_template = ('default', 10)

    return current_template
