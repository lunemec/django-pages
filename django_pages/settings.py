# -*- encoding: utf-8 -*-

from django.conf import settings


try:
    ADMIN_MEDIA_PREFIX = settings.ADMIN_MEDIA_PREFIX

except AttributeError:
    ADMIN_MEDIA_PREFIX = '/static/admin/'

# where to upload flag images /media/FLAG_UPLOAD_DIR
try:
    FLAG_UPLOAD_DIR = settings.FLAG_UPLOAD_DIR

except AttributeError:
    FLAG_UPLOAD_DIR = settings.MEDIA_ROOT
