from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import nexus
nexus.autodiscover()

urlpatterns = patterns('',
    (r'^', include('landing.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^nexus/', include(nexus.site.urls)),
)
