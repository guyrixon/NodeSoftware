#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^tap/', include('vamdctap.urls')),
    (r'^portal/', include('nodes.cdms.node.urls')),
    # Uncomment this line to include mycdmsadmin if installed
    (r'^mycdmsadmin/', include('nodes.cdms.mycdmsadmin.urls')),

)

handler500 = 'vamdctap.views.tapServerError'
handler404 = 'vamdctap.views.tapNotFoundError'
