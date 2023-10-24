from django.core.management.base import BaseCommand
from app001.models import Article, Commentary


class Command(BaseCommand):
    help = "Get all author's commentaries by article title"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Article title')
        order_help = ('Set ordering parameter: '
                      'article, publication_date')
        parser.add_argument('--order', type=str,
                            help=order_help)
        parser.add_argument('--reverse', action='store_true', help='Reverse order')

    def handle(self, *args, **options):
        title = options.get('title')
        order = options.get('order')
        reverse = options.get('reverse')
        commentaries = []
        if order:
            articles = list(Article.objects.order_by(order).filter(title=title))
            if reverse:
                articles.reverse()
        else:
            articles = list(Article.objects.filter(title=title))

        for article in articles:
            tmp = Commentary.objects.filter(article=article).first()
            if tmp:
                commentaries.append(tmp)
        if commentaries:
            self.stdout.write('\n'.join(map(str, commentaries)))
        else:
            self.stdout.write("Not found")
    # Title 7
