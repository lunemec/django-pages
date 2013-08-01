import os

from . import settings


def actual_path(base_path, file_type, path):

    # make sure the path doesn't begin with a slash
    # (this screws up os.path.join)
    if len(path) > 0 and path[0] == '/':
        path = path[1:]

    actual = os.path.abspath(os.path.join(base_path, file_type, path))

    # make sure we end with a slash
    if actual[-1] != '/':
        actual = actual + '/'

    return actual


def actual_url(base_url, file_type, path, filename=None):
    """Return the full URL of the resource; this is the base_url
    (usually settings.FCK_CONNECTOR_URL), with a subsequent path of
    /file_type/path."""

    # we need to remain sane in the face of slashes -- this is especially
    # true when the media type is mapped to root, and we're viewing the
    # root.

    # so the base_url should *not* end in a slash,
    # the file_type should *both* begin and end with a slash,
    # and the path should *not* begin with a slash

    if base_url[-1] == '/':
        base_url = base_url[:-1]

    if len(file_type) == 0:

        file_type = '/'

    if file_type[0] != '/':

        file_type = '/%s' % file_type

    if file_type[-1] != '/':

        file_type = '%s/' % file_type

    if len(path) > 0 and path[0] == '/':
        path = path[1:]

    folder_path = "%s%s%s" % (base_url, file_type, path)

    if filename is not None:
        # append the filename
        if folder_path[-1] != '/':
            folder_path = "%s/%s" % (folder_path, filename)
        else:
            folder_path = "%s%s" % (folder_path, filename)

    return folder_path


def get_resource_type_folder(request):
    """Map a resource_type passed in from the Request to the real
    sub-folder using the RESOURCE_TYPE_MAP.  Returns a tuple containing
    the specified resource type and the mapped path.  If a mapping
    does not exist, the mapped path defaults to the specified
    resource type."""

    resource_type = request.REQUEST.get('Type', None)
    resource_type_path = settings.RESOURCE_TYPE_MAP.get(resource_type,
                                                        resource_type)

    return (resource_type, resource_type_path)
