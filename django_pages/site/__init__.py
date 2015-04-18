# -*- encoding: utf-8 -*-

from ..common.errors import ConfigurationError
from .models import Site, Script


def get_site():
    """
    checks for site with pk=1

    @return Site object
    @raises ConfigurationError
    """
    try:
        site = Site.objects.get(pk=1)
        return site

    except Site.DoesNotExist:
        raise ConfigurationError('There are no Site\'s, please create one in admin')

    except Site.MultipleObjectsReturned:
        raise ConfigurationError('There is more than one site, please make sure there is exactly one, this feature may be changed in future')


def get_scripts():
    """
    Returns all scripts from DB
    """
    return Script.objects.all()
