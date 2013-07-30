from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'', include('django_pages.urls')),
    ) 
