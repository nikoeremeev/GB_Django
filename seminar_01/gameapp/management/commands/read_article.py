from django.core.management.base import BaseCommand
from gameapp.models import Article, Author


class Command(BaseCommand):
    help = "Read article by ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID for update article.')

    def handle(self, *args, **options):
        pk = options.get('pk')
        article = Article.objects.filter(pk=pk).first()
        self.stdout.write(f'{article}')
