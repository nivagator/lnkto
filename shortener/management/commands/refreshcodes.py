from django.core.management.base import BaseCommand, CommandError

from shortener.models import LnktoURL

class Command(BaseCommand):
    help = 'regenerates fresh shortcodes for all urls'

    # def add_arguments(self, parser):
    #     parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        # print(options)
        return LnktoURL.objects.refresh_shortcodes()
 