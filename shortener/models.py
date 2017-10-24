from django.db import models

# Create your models here.

class LnktoURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)


    def __str__(self):
        return str(self.url)

    # def get_shortcode(self):
    #     return(self.url)

