from django.core.management.base import BaseCommand
from app001.models import Article, Author


class Command(BaseCommand):
    help = 'Delete article by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article to delete ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        article = Article.objects.filter(pk=pk).first()
        article.delete()
        self.stdout.write(f'{article}')
