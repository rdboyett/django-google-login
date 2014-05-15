from django.conf.urls import patterns, include, url


urlpatterns = patterns('google_login.views',
    (r'^login/$', 'index'),
    (r'^ajaxAuth/$', 'ajaxAuth'),
    (r'^auth/$', 'auth'),
    (r'^oauth2callback/$', 'auth_return'),
    (r'^logout/$', 'logout'),
    (r'^success/$', 'success'),
    (r'^error/$', 'error'),
)