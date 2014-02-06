from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# static() is here only for developent, so django's runserver serves MEDIA
# DELETE FROM PRODUCTION!

admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admindoc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django_pages.urls')),
)
