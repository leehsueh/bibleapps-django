from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$',
	        'bibleapps.janrain.views.test'
	    ),
    url(r'^login/$',
        'bibleapps.janrain.views.login',
        name='janrain-login'
    ),
    url(r'^logout/$',
        'bibleapps.janrain.views.logout',
        name='janrain-logout'
    ),
)