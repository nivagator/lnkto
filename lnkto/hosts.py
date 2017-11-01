from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    # host(r'(\w+)', 'lnkto.hostconf.urls', name='wildcard2'),
    #host(r'live', 'lnkto.hostconf.urls', name='live-redirect'),
    host(r'(?!www).*', 'lnkto.hostconf.urls', name='wildcard'),
)


