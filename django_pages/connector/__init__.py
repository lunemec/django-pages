"""

==========================
FCKeditor Django Connector
==========================

 :Author: Nathan R. Yergler <nathan@yergler.net>
 :Copyright: 2006-2007
 :License: GNU LGPL; see LICENSE for details.
 :Version: $Rev$
 :Updated: $Date: 2006-08-17 11:57:00 -0400 (Thu, 17 Aug 2006) $

.. contents:: Document Index
    :class: docindex

Overview
--------

 FCKeditor_ is a Javascript-based rich text editor for web applications.  One
 of the enhanced features it offers is a web-based browser for media
 files stored on the server.  The browser relies on a server-side
 *connector* to provide XML responses for commands.  FCKeditor includes
 connectors for many server-side technologies, including a Python CGI
 implementation.  However, when using FCKeditor in a Django_ application,
 it is desirable to implement the connector within the Django process.  This
 package provides a Django-based implementation of the FCKeditor
 `server side specification`_.

Dependencies
------------

 The FCKeditor Connector relies on Django and ElementTree_.  Note that if
 you prefer to use lxml_, you can simply modify the import at the top
 of ``views.py`` from::

   from elementtree import ElementTree

 to::

   import lxml.etree as ElementTree

 
Usage
-----

 To use the FCKeditor Connector you must install the connector as a Django
 application in your project, connect the appropriate URLs, modify the
 admin interface to use FCKeditor and finally update the FCKeditor
 configuration to point to the connector.

Installing the Application
++++++++++++++++++++++++++

 To install the application, simply place the ``fckeditor_connector``
 package on your PYTHONPATH and add ``fckeditor_connector`` to the
 ``INSTALLED_APPS`` setting in ``settings.py``.

 After installing the application you need to set two configuration
 variables found in ``views.py``.  ``BASE_PATH`` defines the base
 file-system path for FCKeditor-browsable files.  Note that FCKeditor
 expects that this directory will contain sub-directories for specific
 file types.  For example, if ``BASE_PATH`` is set to ``/var/www/media``,
 FCKeditor expects that ``/var/www/media/Images`` will contain image files.
 See the `server side specification`_ for details on FCKeditor file paths.

 ``BASE_URL`` should contain the base URL for the files served.  This has
 only been tested with files served from the same server URL as Django
 (using the `static files` Django view for development).

Connecting the URLs
+++++++++++++++++++

 To enable the FCKeditor Connector URLs in your project, you can add
 something like::

    ...
    
    (r'^fckeditor_connector/', include('fckeditor.connector.urls')),

    ...

 to your project ``urls.py``.  If you want to use a different prefix, you'll
 need to use that instead of ``fckeditor_connector`` when configuring
 FCKeditor below.
 
Configuring FCKeditor
+++++++++++++++++++++

 To enable FCKeditor to use the Django connector, you need to update
 ``fckconfig.js`` to point to the connector.  The default FCKeditor
 connector configuration is based on a standard URL schema.  Unfortunately
 this does not work with the Django connector, so we have to specify a
 complete URL.  In ``fckconfig.js`` you will find a block on configuration
 parameters such as::
 
   FCKConfig.ImageBrowser = true ;
   FCKConfig.ImageBrowserURL = FCKConfig.BasePath + 'filemanager/browser/default/browser.html?Type=Image&Connector=connectors/' + _FileBrowserLanguage + '/connector.' + _FileBrowserExtension ;
   FCKConfig.ImageBrowserWindowWidth  = FCKConfig.ScreenWidth * 0.7 ;	// 70% ;
   FCKConfig.ImageBrowserWindowHeight = FCKConfig.ScreenHeight * 0.7 ;	// 70% ;

 Below this block add the following line::
 
   FCKConfig.ImageBrowserURL = FCKConfig.BasePath + 'filemanager/browser/default/browser.html?Type=Image&Connector=/fckeditor_connector/browser/';

 Note that if you did not use the suggested URL prefix you will need to
 modify this line.  In particular, the first portion of the ``Connector``
 query string parameter should contain the base URL provided in your project's
 ``urls.py``.

Using FCKeditor in the Admin interface
++++++++++++++++++++++++++++++++++++++

 There are several ways to connect the FCKeditor to the Admin interface.  The
 way we have tested with is to replace a specific ``textarea``.  To use the
 FCKeditor, you need to download FCKeditor and put it in a location
 accessible by Django.  Currently we put this underneath the admin
 media directory.  Once you have it accessible, you need to add the following
 information to the ``Admin`` class of the appropriate model::

     class Admin:
        # javascript for fck editor
        js = ( 'underlay/fckeditor/fckeditor.js',
               'underlay/news/story.js',
               )


 In this case ``story.js`` is a small Javascript file which contains the
 following::

     window.onload = function()
     {
         // create the FCK Editor and replace the specific text area with it
         var oFCKeditor = new FCKeditor( 'id_text' ) ;
         oFCKeditor.BasePath	= '/underlay/fckeditor/'; 
         oFCKeditor.ReplaceTextarea() ;
     }

 Note that ``id_text`` is the name of the TextField in your model prepended
 with ``id``.  The ``BasePath`` setting should reflect the absolute path you
 used to make the FCKeditor files available.

Known Issues
------------

 The Connector currently only implements File Browser Connector at this point.
 The `Quick Uploader`_ API will be implemented in the future.

 Permission problems are not correctly reported.

Contact Information
-------------------


.. _FCKeditor: http://www.fckeditor.net
.. _Django: http://djangoproject.com
.. _`server side specification`: http://wiki.fckeditor.net/Developer%27s_Guide/Participating/Server_Side_Integration#Browser
.. _ElementTree: http://effbot.org/zone/element-index.htm
.. _lxml: http://codespeak.net/lxml
.. _`static files`: http://www.djangoproject.com/documentation/static_files/
.. _`Quick Uploader`: http://wiki.fckeditor.net/Developer%27s_Guide/Participating/Server_Side_Integration#Upload

"""


try:
    from elementtree import ElementTree
except ImportError:
    try:
        import lxml.etree as ElementTree
    except ImportError:
        raise ImportError, "Neither elementtree.ElementTree nor lxml.etree was found. This is required by fckeditor_connector"
