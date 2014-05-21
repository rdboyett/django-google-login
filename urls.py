from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/google/login'}),
)

urlpatterns += patterns('google_login.views',
    (r'^login/$', 'index'),
    (r'^auth/$', 'auth'),
    (r'^oauth2callback/$', 'auth_return'),
    (r'^success/$', 'success'),
    (r'^error/$', 'error'),
    (r'^forgot/(?P<forgotID>\d+)/$', 'forgotPassword'),
    (r'^passwordReset/$', 'passwordReset'),

#------------------ajax calls -------------------------------------
    url(r'^ajaxAuth/$', 'ajaxAuth', name='ajaxAuth'),
    url(r'^checkUsername/$', 'checkUsername', name='checkUsername'),
    url(r'^submitRegistration/$', 'submitRegistration', name='submitRegistration'),
    url(r'^doesEmailExist/$', 'doesEmailExist', name='doesEmailExist'),
    url(r'^submitPasswordForgot/$', 'submitPasswordForgot', name='submitPasswordForgot'),
    
)
