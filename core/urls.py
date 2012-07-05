from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import nexus
nexus.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    (r'^', include('landing.urls')),
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('cms.urls')),
    (r'^nexus/', include(nexus.site.urls)),
)


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns