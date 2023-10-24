from django.core.management.base import BaseCommand
from app001.models import Article, Author
from datetime import date
from random import randint


class Command(BaseCommand):
    help = "Add fake articles."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of fake articles.')

    def handle(self, *args, **options):
        amount = options.get('amount')
        for i in range(1, amount + 1):
            author = Author(
                name=f'Author Nm{i}',
                surname=f'Author Snm{i}',
                email=f'mail{i:0>4}@mail.com',
                biography=f'{i}\'s Lorem biography',
                birthday=date.today()
            )
            author.save()
            for j in range(1, amount):
                article = Article(
                    title=f'Title {j}',
                    content='Lorem ipsum ' * j * amount,
                    author=author,
                    category=f'{randint(1, 5)}',
                )
                article.save()
                