import os.path
import urlparse
from django.conf import settings

# See __init__.py for documentation on setting the values of
# FCKEDITOR_CONNECTOR_ROOT and FCKEDITOR_CONNECTOR_URL

# FCKEDITOR_CONNECTOR_PREFIX defines the path prefix inserted between
# the MEDIA_ROOT and item type (ie, 'Image') when forming the actual path
#
# For example, if MEDIA_ROOT is set to '/var/www', this setting:
#
# FCKEDITOR_CONNECTOR_PREFIX = 'Media'
#
# would cause FCKeditor Connector to look in '/var/www/Media/Image' for
# images when browsing the server.

FCKEDITOR_CONNECTOR_PREFIX = 'uploaded'


FCKEDITOR_CONNECTOR_ROOT = os.path.join(settings.MEDIA_ROOT,
                                        FCKEDITOR_CONNECTOR_PREFIX)
FCKEDITOR_CONNECTOR_URL = urlparse.urljoin(settings.MEDIA_URL,
                                        FCKEDITOR_CONNECTOR_PREFIX)


# RESOURCE_TYPE_MAP allows you to map FCKeditor's resource types
# (Image, File, etc) to other paths; these are still appended to
# both [FCKEDITOR_CONNECTOR_ROOT|FCKEDITOR_CONNECTOR_URL] + PREFIX

RESOURCE_TYPE_MAP = {
    'Image' : 'images',
    'Flash' : 'flash',
    'Media' : 'media',
    'File' : '',
    }

IGNORE_FOLDERS = ['.svn',]
