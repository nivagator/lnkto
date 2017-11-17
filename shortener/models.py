from django.conf import settings
from django.db import models
# from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
# Create your models here.
from .validators import validate_dot_com, validate_url
from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class LnktoURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(LnktoURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = LnktoURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class LnktoURL(models.Model):
    url         = models.CharField(max_length=220, validators=[validate_dot_com, validate_url])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True) #everytime the model is saved
    timestampo  = models.DateTimeField(auto_now_add=True) #when model is created
    active      = models.BooleanField(default=True)
   

    objects = LnktoURLManager()
   

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(LnktoURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        # url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, scheme='http')
        print('url_path - models.py - get_short_url',url_path)
        return url_path