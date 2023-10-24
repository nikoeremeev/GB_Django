from django.core.management.base import BaseCommand
from app001.models import Article, Author


class Command(BaseCommand):
    help = "Get all author's articles by author surname and name"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')
        parser.add_argument('surname', type=str, help='Author surname')
        parser.add_argument('--amount', type=int,
                            help='Amount of records')
        order_help = ('Set ordering parameter: '
                      'title, category, views, '
                      'publication_date, published')
        parser.add_argument('--order', type=str,
                            help=order_help)
        parser.add_argument('--reverse', action='store_true', help='Reverse order')

    def handle(self, *args, **options):
        surname = options.get('surname')
        name = options.get('name')
        amount = options.get('amount') or 0
        order = options.get('order')
        reverse = options.get('reverse')
        author = Author.objects.filter(surname=surname, name=name).first()
        if author:
            if order:
                if reverse:
                    articles = list(
                        Article.objects.order_by(order).filter(author=author)
                    )[::-1][-amount:]
                else:
                    articles = list(
                        Article.objects.order_by(order).filter(author=author)
                    )[-amount:]
            else:
                articles = list(Article.objects.filter(author=author))[-amount:]
            self.stdout.write('\n'.join(
                [
                    f'Articles by {author.get_fullname()}:',
                    '\n'.join(map(str, articles)),
                ]
            ))
        else:
            self.stdout.write("Not found")
        # Author Nm2 Author Snm2
