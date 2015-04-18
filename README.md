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

Get this application:

    pip install django-pages 

Create your project:

    Install Django (pip install django)
    Create your Django application 

Configure
---------

`settings.py`

    # For better admin interface, add the dashboard:
    GRAPPELLI_INDEX_DASHBOARD = 'django_pages.dashboard.DjangoPagesDashboard'

    # Add grappelli, filebrowser and django_pages to INSTALLED_APPS:
    INSTALLED_APPS = (
        'grappelli.dashboard',
        'grappelli',
        ...
        'filebrowser',
        'django_pages'
    )

    # Set proper MEDIA_ROOT path, and create uploads directory inside.

Your `urls.py` should contain roughly this, note that django_pages urls MUST be
the last:

    urlpatterns = patterns(
        '',
        # this is to enable nice looks in admin
        url(r'^grappelli/', include('grappelli.urls')),

        # admin site itself - recommended
        url(r'^admin/', include(admin.site.urls)),

        # django-pages url resolver - required
        url(r'', include('django_pages.urls')),
    )

Create empty `database`:

    python manage.py migrate

Add superuser:

    python manage.py createsuperuser

Run webserver:

    run your webserver (nginx/apache/django test server)

Add some nice website content:

    go to http://your_site/admin/ and create structure

    Use your new webpage!


Configuration
-------------
You can override default settings on these values:

`ADMIN_MEDIA_PREFIX` = '/static/admin/'
This is where django will look for admin static files (for deployment with collectstatic)

`FLAG_UPLOAD_DIR` = settings.MEDIA_ROOT + '/languages'
This is wher language flags will be saved and loaded from

`POSTS_ON_PAGE` = 10
How many posts on page show

Optional:
Set `DEBUG` = True in settings.py while creating pages to see debugging information


Create website
--------------
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
* Disable active on the page you're working on and save it.
* Click on preview and you can see the resulting page.
* When you're satisfied with it, set it to active again.


Adding Images
-------------
You can now add images directly from admin. Select Page/Post you want to edit. Click on Image icon in the editor.
Click Browse server. In the new window, either upload your image or select
already uploaded image from the files.

Once selected, Image will be automatically selected by the editor, and you can hit OK.
It will automatically create link for that image.

Files will be uploaded to your `MEDIA_ROOT` path into folder uploaded 
(you can change this in file connector/settings.py - I'm working on making this easier)

Don't forget to set your /media/uploaded/ folder permissions to 775 so you'll be able to save images into it from admin!


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
1. In your settings.py, set `TEMPLATE_PATH` = 'templatename'
2. Copy templates/default to templates/templatename
3. Edit files in templates/templatename to your liking
4. Save your css/js inside your project's /static/ and in base_static.html change path and names inside {% static 'filename' %}

Note: all commands inside {} are django template language, and I suggest you leave it as is, and just change the HTML surrounding it.

I wanted to make templatetags that would just say {% menu %}, {% content %} {% comments %}, but each of these requires some HTML to render them, so it will be as it is for now.


Scheme
------
Application and database scheme:

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

`http://mydomain.example/language/my-page-with-somethin~page_number/~post`

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
    /rss/
    /atom/
    /robots.txt
    /sitemap.xml


Caching
-------
Django_pages now supports caching in-memory, for some reason django's wrapper @chache_page for specific view caching works without CACHE in settings.py, which is weird at least. I tried memcached, in-memory and without cache, and in-memory had the best results, and you don't even have to configure it.
Now it can handle 50 concurrent page acceses in 12ms! (tested with ab -n 1000 -c 50 http://nemec.lu/)


Atom and RSS
------------
Atom and RSS are accessible under /atom/ and /rss/ respectively.
Simply add one record into admin Feed Settings, it must contain Site Title, Site Description, and latest post count.
You can disable rss and atom feed by disabling it in admin.
Any new Posts under any menu/menuitem will be shown in rss/atom feed from newest to oldest.
