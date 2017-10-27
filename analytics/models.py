from django.db import models

# Create your models here.
from shortener.models import LnktoURL

class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, LnktoURL):
            obj, created = self.get_or_create(lnkto_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    lnkto_url   = models.OneToOneField(LnktoURL) 
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True) 
    timestampo  = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return '{i}'.format(i=self.count)