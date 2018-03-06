from django.core.management.base import BaseCommand, CommandError
from cards.models import WatermarkUser as User, Wallet, Profile

class Command(BaseCommand):
    help = 'Populates database with users.'

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int)

    def handle(self, *args, **options):
        print(options)