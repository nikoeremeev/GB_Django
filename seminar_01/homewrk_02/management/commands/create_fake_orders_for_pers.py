from django.core.management.base import BaseCommand
from homewrk_02.models import Product

from faker import Faker
from random import sample, randint as rin, uniform
from string import ascii_uppercase as letters

fake = Faker()


class Command(BaseCommand):
    help = "Generate some fake products."

    def add_arguments(self, parser):
        parser.add_argument('amt', type=int, help='Amount of fake users to generate.')

    def handle(self, *args, **options):
        amt = options.get('amt')
        for _ in range(amt):
            Product(
                name=f'article {"".join(sample(letters, 3))}.{rin(1, 99):0>3}-{rin(11, 999):0>3}',
                description=fake.text(300),
                price=uniform(99, 99999),
                amount=rin(10, 300),
            ).save()
        self.stdout.write(f"Added {amt} products.")