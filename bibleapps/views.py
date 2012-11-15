from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))

def env_info(request):
    import sys
    import django
    return HttpResponse(sys.version + '<br>' + django.get_version())