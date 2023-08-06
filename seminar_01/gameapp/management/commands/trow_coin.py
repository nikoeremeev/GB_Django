from django.core.management.base import BaseCommand
from gameapp.models import Coin
import random


class Command(BaseCommand):
    help = "Trow a coin."

    def handle(self, *args, **kwargs):
        Coin.add_trow(random.choice(["obverse", "reverse"]))
