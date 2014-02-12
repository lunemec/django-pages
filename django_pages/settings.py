# -*- encoding: utf-8 -*-

"""
This settings file is used to override your project's settings with
some defaults required to run django-pages
"""

from django.conf import settings


ADMIN_MEDIA_PREFIX = getattr(settings, 'ADMIN_MEDIA_PREFIX', '/static/admin/')

# where to upload flag images /media/FLAG_UPLOAD_DIR
FLAG_UPLOAD_DIR = getattr(settings, 'FLAG_UPLOAD_DIR', settings.MEDIA_ROOT)
