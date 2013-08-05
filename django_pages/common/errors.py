# -*- encoding: utf-8 -*-

"""
Custom errors definition
"""

from django.core.exceptions import ImproperlyConfigured


class ConfigurationError(ImproperlyConfigured):

    def __init__(self, *args, **kwargs):

        super(ConfigurationError, self).__init__(*args, **kwargs)
