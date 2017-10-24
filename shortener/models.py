import random
import string
from django.db import models

# Create your models here.

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class LnktoURL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15, unique=True)
    updated     = models.DateTimeField(auto_now=True) #everytime the model is saved
    timestampo  = models.DateTimeField(auto_now_add=True) #when model is created
    # empty_datetime = models.DateTimeField(auto)

    def save(self, *args, **kwargs):
        print("something")
        self.shortcode = code_generator()
        super(LnktoURL, self).save(*args, **kwargs)

    

    def __str__(self):
        return str(self.url)

    # def get_shortcode(self):
    #     return(self.url)

