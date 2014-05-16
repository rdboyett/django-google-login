from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/google/login'}),
)

urlpatterns += patterns('google_login.views',
    (r'^login/$', 'index'),
    url(r'^ajaxAuth/$', 'ajaxAuth', name='ajaxAuth'),
    (r'^auth/$', 'auth'),
    (r'^oauth2callback/$', 'auth_return'),
    (r'^success/$', 'success'),
    (r'^error/$', 'error'),
)
