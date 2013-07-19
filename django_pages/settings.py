# -*- encoding: utf-8 -*-

from django.conf import settings


ADMIN_MEDIA_PREFIX = '/static/admin/'

# where to upload flag images /media/FLAG_UPLOAD_DIR
FLAG_UPLOAD_DIR = settings.MEDIA_ROOT

# where to look for template in templates/
TEMPLATE_PATH = 'default'

POSTS_ON_PAGE = 10
