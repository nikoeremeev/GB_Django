from django.core.management.base import BaseCommand
from app001.models import Author, Commentary


class Command(BaseCommand):
    help = "Get all author's commentaries by author ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        author = Author.objects.filter(pk=pk).first()
        commentaries = Commentary.objects.filter(author=author)
        self.stdout.write('\n'.join(
            [
                f'Commentaries by {author.get_fullname()}:',
                '\n'.join(map(str, commentaries))
            ]
        ))
