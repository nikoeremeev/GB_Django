from django.core.management.base import BaseCommand
from gameapp.models import Article, Author
from datetime import datetime


class Command(BaseCommand):
    help = "Add fake articles."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of fake articles.')

    def handle(self, *args, **options):
        amount = options.get('amount')
        for i in range(1, amount + 1):
            author = Author(
                name=f'name{i}',
                surname=f'surname{i}',
                email=f'mail{i}@mail.ru',
                biography=f'biography{i}',
                birthday=datetime.today()
            )
            author.save()
            for j in range(1, amount + 1):
                article = Article(
                    title=f'title{j}',
                    content=f'content{j}',
                    author=author,
                    category=f'category{j}'
                )
                article.save()
