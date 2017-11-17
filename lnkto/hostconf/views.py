from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.lnkto.co")

def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REDIRECT_URL
    print(new_url)
    print('Path1',path,'test')
    if path is not None:
        print('Path2',path,'path is not none')
        new_url = DEFAULT_REDIRECT_URL + "/" + path
        print(new_url)
    return HttpResponseRedirect(new_url)