from django.conf import settings
from django_hosts import patterns, host
from lnkto.hostconf import urls as redirect_urls

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'lnkto.hostconf.urls', name='wildcard'),
)