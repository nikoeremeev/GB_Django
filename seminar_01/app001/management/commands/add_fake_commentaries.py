from django.core.management.base import BaseCommand
from app001.models import Article, Author, Commentary
from random import randint, choice, sample


class Command(BaseCommand):
    help = "Add fake commentaries."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of fake articles.')

    def handle(self, *args, **options):
        amount = options.get('amount')
        authors = sample(list(Author.objects.all()), amount)
        articles = sample(list(Article.objects.all()), amount)
        comments = []
        for author in authors:
            comments.append(
                Commentary(
                    author=author,
                    article=(tmp := articles.pop()),
                    content=f'Int {tmp.title} there is {"Lorem ipsum " * randint(3, 8)}'
                )
            )
            comments[-1].save()
        self.stdout.write('\n'.join([*map(str, comments)]))

