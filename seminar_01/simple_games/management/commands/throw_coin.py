from django.core.management.base import BaseCommand
from simple_games.models import CoinPlay
from random import randint


class Command(BaseCommand):
    help = "Throw a coin."

    def handle(self, *args, **options):
        coin = CoinPlay(**CoinPlay.add_throw(randint(0, 1)))
        coin.save()
