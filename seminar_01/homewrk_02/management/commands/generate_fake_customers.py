from django.core.management.base import BaseCommand
from homewrk_02.models import Customer

from faker import Faker
from random import sample, choice, randint as rin
from string import ascii_lowercase as letters

DOMAINS = ["com", "info", "net", "org", "gov", "ru", "cc"]

fake = Faker()
ru_fake = Faker("RU-ru")


class Command(BaseCommand):
    help = "Generate some fake customers."

    def add_arguments(self, parser):
        parser.add_argument('amt', type=int, help='Amount of fake users to generate.')

    def handle(self, *args, **options):
        amt = options.get('amt')
        for _ in range(amt):
            Customer(
                name=f'{(nm := fake.name())}',
                email=f'{".".join(nm.split())}@{"".join(sample(letters, rin(4, 10)))}.{choice(DOMAINS)}',
                phone=f'{ru_fake.phone_number()}',
                address=f'{ru_fake.address()}',
                reg_date=f'{rin(2021, 2022)}{fake.date("-%m-%d")}',
            ).save()
        self.stdout.write(f"Added {amt} customers.")
