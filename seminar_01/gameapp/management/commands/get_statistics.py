from django.core.management.base import BaseCommand
from gameapp.models import Coin
import random


class Command(BaseCommand):
    help = "Trow a coin."

    def add_arguments(self, parser):
        parser.add_arguments('amount', type=int, help='Amount of last trows')

    def handle(self, *args, **options):
        amount = options.get('amount')
        stat_dict = Coin.get_trows(amount)
        self.stdout.write(stat_dict)
