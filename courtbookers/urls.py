from django.conf.urls import patterns, include, url
from .views import root_view, home_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', root_view, name="root"),
    url(r'^home/$', home_view, name="home"),
    # url(r'^$', 'courtbookers.views.home', name='home'),
    # url(r'^courtbookers/', include('courtbookers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
