from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bibleapps.views.home', name='home'),
    # url(r'^bibleapps/', include('bibleapps.foo.urls')),
    # NT greek app
    (r'^ntgreek/', include('bibleapps.ntgreekvocab.urls', namespace='ntgreekvocab', app_name='ntgreekvocab')),

    # Bible tidbits app
    (r'^tidbits/', include('bibleapps.bible_tidbits.urls', namespace='tidbits', app_name='bible_tidbits')),

    # evernote oauth app
    (r'^evernote/oauth/', include('bibleapps.evernote_oauth.urls', namespace='evernote_oauth', app_name='evernote_oauth')),
    
    # evernote reftagger
    (r'^evernote_reftagger/', include('bibleapps.evernote_reftagger.urls', namespace='evernote_reftagger', app_name='evernote_reftagger')),
    
    # google oauth
    (r'^google_oauth/', include('bibleapps.google_oauth.urls', namespace='google_oauth', app_name='google_oauth')),

    # google reftagger
    (r'^google_docs_reftagger/', include('bibleapps.google_docs_reftagger.urls', namespace='google_docs_reftagger', app_name='google_docs_reftagger')),

    # user accounts
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'janrain_login.html'}, name='login'),
    url(r'^accounts/logout/$', 'bibleapps.views.logout_view', name='logout'),
    url(r'^accounts/pc/$', 'django.contrib.auth.views.password_change', name='passwd-change'),
    url(r'^accounts/pc/done/$', 'django.contrib.auth.views.password_change_done', name='passwd-change-done'),

    # janrain login urls
    url(r'^janrain/', include('bibleapps.janrain.urls', namespace='janrain', app_name='janrain')),

    url(r'^env_info/$', 'bibleapps.views.env_info', name='env-info'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.MEDIA_ROOT}),
    )