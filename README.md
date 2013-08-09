Django-pages
===========================

About this project
------------------

This project will give you the power of standard CMS (content management system) like Drupal, Joomla, WordPress but with much more speed and simplicity.

It may not have as much plugins and templates like WordPress but it is super simple application with django admin with WYSIWYG editors for page and post editing.

It is designed for easy web content editing with no previous experience in HTML or CSS. Just install it once, use default template or create one for yourself (or hire someone to make it) and use it. There is no maintenance required.

This project is running on this site: [Nemec.lu](http://nemec.lu/)

Installation
------------

Note: do NOT use settings.py from sample_project! the secret key is visible to all and it is a security risk. Create your own Django application and simply fill settings depending on your configuration.

Get this application:

    pip install django-pages 

Install dependencies:
    
    pip install -r DEPENDENCIES

Create your project:

    Install Django (pip install django)
    Create your Django application (see [django docs](https://docs.djangoproject.com/en/1.5/intro/install/))

    OR

    Download and copy somewhere the sample_project

Configure:

    # add to settings.py:
    USE_TZ = True

# don't forget to include django admin in INSTALLED_APPS

    # add to INSTALLED_APPS:
    'django_pages',
    'django_pages.comments',
    'django_pages.common',
    'django_pages.connector',
    'django_pages.feed',
    'django_pages.language',
    'django_pages.log',
    'django_pages.looks',
    'django_pages.menu',
    'django_pages.metadata',
    'django_pages.pages',
    'django_pages.site',
    'reversion',

    # optional
    'grappelli', <- nice admin looks

    
    # add to MIDDLEWARE_CLASSES for logging requests into file 
    'django_pages.log.middleware.RequestLog',

    # for logging, also configure logger with name 'requestlog'
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'log': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': 'request.log',
                'when': 'D',
                'interval': 1,
            }
        },
        'loggers': {
                'requestlog': {
                'handlers': ['log',],
                'level': 'INFO',
            }   
        }
    }


Add this to your urls.py:

        # optional for nice admin look (must be above django_pages):
        url(r'^grappelli/', include('grappelli.urls')),

        url(r'', include('django_pages.urls')),

Create empty database:
    
    run #~ python manage.py syncdb  to create database and tables
    
Run webserver:
    
    run your webserver (nginx/apache/django test server)

Add some nice website content:

    go to http://your_site/admin/ and create structure

    Use your new webpage!


Configuration
-------------

You can override default settings on these values:

ADMIN_MEDIA_PREFIX = '/static/admin/'
This is where django will look for admin static files (for deployment with collectstatic)

FLAG_UPLOAD_DIR = settings.MEDIA_ROOT + '/languages'
This is wher language flags will be saved and loaded from

POSTS_ON_PAGE = 10
How many posts on page show

Optional:
Set DEBUG = True in settings.py while creating pages to see debugging information


Create website
--------------

**Or use the new Wizzard (go to http://yoururl.example/wizzard/)**

    Go to http://mydomain.example/admin/ (replace mydomain.example with your actual domain)
    
    Login using credentials from command python manage.py syncdb

    Create Site

    Create Language(s)

    Create MenuItems with good url (for SEO) for Menu # example: my-page-that-displays-how-to-cook

    Create exactly 1 Page with index set to True

    Create Pages with content pointing to MenuItems which create link to that Page

    Set Language, Page and others as Active to be displayed

    Create 1 Feed Setting, either with information or just deactivated feed (RSS and Atom feed setting)

    Optional:
    Create Posts on Page (optional: set duration for Post visibility)

    SEO:
    Create MetaSets for Pages
    Create MetaData for MetaSets

    Set DEBUG = False in you settings.py after succesfull creation!

    Done!


Preview in admin
----------------

The preview does this:
    
    After clicking on Preview, it sets the item to INACTIVE
    Displays it as it would look on the page (pagination may not work)
    
DO NOT FORGET to set the item to ACTIVE after you're happy with the way it looks!!!


Wizzard
-------

This is just a simple helper page, that will guide you through the process of creating your presentation.
Images and exmplanations included.

Wizzard is accesible from http://yoursite.com/wizzard/


Adding Images
-------------

You can now add images directly from admin. Select Page/Post you want to edit. Click on Image icon in the editor.
Click Browse server. In the new window, either upload your image (will be automatically resized to fit 800x600 px) or select
already uploaded image from the files.

Once selected, Image will be automatically selected by the editor, and you can hit OK.
It will automatically create link for that image.

If you want this image to have nice pop-up effects from Lightbox2, click on small magnifiing glass icon (Create Lightbox),
insert text you want the image to have and click OK.

Files will be uploaded to your MEDIA_ROOT path into folder uploaded (you can change this in file connector/settings.oy)

Don't forget to set your /media/uploadeded/ folder permissions to 775 so you'll be able to save images into it from admin!


Templates
---------

You can now use one of 3 default templates!

The default, which is the first that came with this package, just ordinary white and responsive design,
default2 is white design based on twitter bootstrap from bootswatch.com, (default theme)
default3 is black design based on twitter bootstrap from bootswatch.com (cyborg theme).

To use any of the builtins, create new item in Admin/Looks/Templates, type in the name (default, default2, default3)
and number of posts to display on page.

Note: You need to fiddle with the number of posts, depending on your average post heading length, sometimes
when you have long titles, the submenu displaying posts just doesn't work properly.

Copy your custom template into your project's templates folder, and add Template in admin's Looks subsection
and set it to active, the system will use your new template automatically.

Note: there is a 30s cache for current template, so after the change in admin, wait a bit for it to display.


Creating custom template
------------------------

1. In your settings.py, set TEMPLATE_PATH = 'templatename'
2. Copy templates/default to templates/templatename
3. Edit files in templates/templatename to your liking
4. Save your css/js inside your project's /static/ and in base_static.html change path and names inside {% static 'filename' %}

Note: all commands inside {} are django template language, and I suggest you leave it as is, and just change the HTML surrounding it.

I wanted to make templatetags that would just say {% menu %}, {% content %} {% comments %}, but each of these requires some HTML to render them, so it will be as it is for now.


Scheme
------

Wysiwyg editor uses this application and database scheme

    Site
    Language --> 
        {Multiple menuitems} --> 
            [Page for each menuitem] --> 
                (Multiple Posts for each Page - with pagination) -->
                    (Multiple comments for each Post)
            [MetaSet for each page] -->
                (Multiple MetaData for each MetaSet)

Url
---

Url is following:

    http://mydomain.example/language/my-page-with-somethin~page_number/~post
    
Rules are following:

    language - string with 2-3 letters
    page - 4-200 letters where allowed is alphabet, digits and - . _
    page_number - digits
    post - same as page

Note: all of this is generated automatically from DB, you provide country_code for your language
which is used as /language part of url. MenuItem url is used as Page url part. Page_number is determined
automatically from post count. Post detail url is determined automatically from post title - alphabet lowercase
with rules same as page.

Reserved URLs:
    
    /admin/*
    /connector/*
    /grapelli/*
    /wizzard/
    /rss/
    /atom/
    /robots.txt
    /sitemap.xml


Caching
-------

Wysiwyg now supports caching in-memory (I guess), for some reason django's wrapper @chache_page for specific view caching works without CACHE in settings.py, which is weird at least. And I tried memcached, in-memory and without cache, and in-memory had the best results, and you don't even have to configure it.
Now it can handle 50 concurrent page acceses in 12ms! (tested with ab -n 1000 -c 50 http://lnemec.tk/)


Atom and RSS
------------

Atom and RSS are accessible under /atom/ and /rss/ respectively.
Simply add one record into admin Feed Settings, it must contain Site Title, Site Description, and latest post count.
You can disable rss and atom feed by disabling it in admin.
Any new Posts under any menu/menuitem will be shown in rss/atom feed from newest to oldest.
