from django.core.management.base import BaseCommand
from simple_games.models import CoinPlay


class Command(BaseCommand):
    help = "Get stats on throws."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int,
                            help='Amount of last throws (0 for all throws).')

    def handle(self, *args, **options):
        amount = options.get('amount')
        aggregate = {'obverse': 0, 'reverse': 0}
        for a_throw in list(CoinPlay.objects.all())[-amount:]:
            if a_throw.side == 'obverse':
                aggregate['obverse'] += 1
            else:
                aggregate['reverse'] += 1
        self.stdout.write(str(aggregate))
