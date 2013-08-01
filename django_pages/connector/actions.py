import os
import stat
from subprocess import call

from . import ElementTree
from .settings import IGNORE_FOLDERS


def get_folders(xml_response, folder_path):
    """Add information about the folders in [folder_path] to
    [xml_response].
    """

    folders = ElementTree.Element("Folders")

    for f in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, f)) and not f in IGNORE_FOLDERS:
            folders.append(ElementTree.Element("Folder", {'name': f}))
    xml_response.getroot().append(folders)


def get_folders_and_files(xml_response, folder_path):

    folders = ElementTree.Element("Folders")
    files = ElementTree.Element("Files")

    for f in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, f)):
            if not f in IGNORE_FOLDERS:
                folders.append(ElementTree.Element("Folder", {'name': f}))
        else:
            size = os.lstat(os.path.join(folder_path, f))[stat.ST_SIZE]
            size = str(size / 1024)

            files.append(ElementTree.Element("File",
                                             {'name': f,
                                              'size': size}
                                             )
                         )

    xml_response.getroot().append(folders)
    xml_response.getroot().append(files)


def file_upload(request, folder_path):
    """Handle a file upload and return the status code."""

    new_file = request.FILES.get('NewFile', None)
    if new_file is None:
        status = "202"
    else:
        # determine the destination file name
        file_name = new_file.name
        base, ext = os.path.splitext(file_name)
        count = 1

        while (os.path.exists(os.path.join(folder_path, file_name))):
            file_name = '%s(%s)%s' % (base, count, ext)
            count += 1

        # write the file
        target = file(os.path.join(folder_path, file_name), 'wb')
        for chunk in new_file.chunks():
            target.write(chunk)
        target.close()

        file_w_path = os.path.join(folder_path, file_name)

        # set the status
        if file_name == new_file.name:
            status = "0"
        else:
            status = "201"

        return status, file_name
