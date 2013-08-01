import os

from . import ElementTree
from . import settings
from . import actions
from . import support
from .support import actual_path, actual_url

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def browser(request):

    if request.user.is_staff:

        # extract the command, type and folder path
        command_name = request.REQUEST.get('Command', None)

        resource_type, resource_type_path = \
            support.get_resource_type_folder(request)

        folder_path = request.REQUEST.get('CurrentFolder', None)

        # set the default return values to successful completion
        err_no = 0
        err_txt = 'Successful'

        xml_response = ElementTree.ElementTree(
            ElementTree.Element("Connector", {'command': command_name,
                                              'resourceType': resource_type})
        )

        if None in (command_name, resource_type, folder_path):
            err_no = 1
            err_txt = 'Incomplete command.'
        else:
            # construct the response
            # append current folder information
            abs_path = actual_path(settings.FCKEDITOR_CONNECTOR_ROOT,
                                 resource_type_path, folder_path)
            abs_url = actual_url(settings.FCKEDITOR_CONNECTOR_URL,
                                 resource_type_path, folder_path)

            xml_response.getroot().append(
                ElementTree.Element("CurrentFolder",
                                    {'path': folder_path,
                                     'url': abs_url,
                                    }
                )
            )

            if (command_name == 'GetFolders'):
                # append Folder list
                actions.get_folders(xml_response, abs_path)

            elif (command_name == 'GetFoldersAndFiles'):
                # append Folder and list
                actions.get_folders_and_files(xml_response, abs_path)

            elif (command_name == 'CreateFolder'):
                new_folder_name = request.REQUEST.get('NewFolderName', None)

                if new_folder_name is None:
                    err_no = 102
                    err_txt = 'Invalid folder name.'
                else:

                    try:
                        os.mkdir(os.path.join(abs_path, new_folder_name))
                    except Exception, e:
                        err_no = 110
                        err_txt = str(e)

            elif (command_name == 'FileUpload'):

                status, filename = actions.file_upload(request, abs_path)

                if int(status) == 201:
                    # upload through the browser requires a conjoined
                    # status and filename if the file was renamed
                    status = "%s, '%s'" % (status, filename)

                return HttpResponse(
                    """<script type="text/javascript">
                    window.parent.frames['frmUpload'].OnUploadCompleted(%s)
                    </script>""" % status)

            else:
                # unknown command
                xml_response.getroot().append(
                    ElementTree.Element("Error", {'number': 1, 'text': 'blarf'})
                )

        xml_response.getroot().append(
            ElementTree.Element("Error", {'number': str(err_no), 'text': err_txt})
        )

        response = HttpResponse(ElementTree.tostring(xml_response.getroot(),
                                                    'utf-8'),
                                mimetype='text/xml')
        response['Cache-Control'] = 'no-cache'

        return response

    else:

        return None


def uploader(request):
    """Quick Uploader server-side support.  Responds to a POST request
    with the file uploaded as NewFile."""

    if request.user.is_staff:

        # extract the command, type and folder path
        try:
            resource_type, resource_type_path = \
                support.get_resource_type_folder(request)
            if resource_type is None:
                # no type specified
                resource_type_path = ''

            # determine the actual folder path
            folder_path = actual_path(settings.FCKEDITOR_CONNECTOR_ROOT,
                                    resource_type_path, '')

            # handle the upload
            status, filename = actions.file_upload(request, folder_path)

            # calculate the resulting file URL
            file_url = actual_url(settings.FCKEDITOR_CONNECTOR_URL,
                                resource_type_path, '', filename)

        except Exception, e:
            print e
            raise e

        # return an HTML response
        return HttpResponse(
            """<script type="text/javascript">
            window.parent.OnUploadCompleted(%s, '%s', '%s', '')

            </script>""" % (status, file_url, filename,)
        )

    else:

        return None
