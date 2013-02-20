from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import patterns, include, url
import sdjango


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^backend/', include('backend.urls'), name='backend'),
	url(r'^socket.io', include(sdjango.urls)),
	# url(r'^socket.io/', include('backend.urls'), name='backend'),

    # Examples:
    # url(r'^$', 'simplecat.views.home', name='home'),
    # url(r'^simplecat/', include('simplecat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    )

urlpatterns += staticfiles_urlpatterns()
