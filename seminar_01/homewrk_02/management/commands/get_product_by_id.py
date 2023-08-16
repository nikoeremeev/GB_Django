from django.core.management.base import BaseCommand
from homewrk_02.models import Product


class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Searched product ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        if prod := Product.objects.filter(pk=pk).first():
            out_string = ('=' * 80 +
                          f'\n{"Product id:":.<20}{prod.pk}\n'
                          f'{"Name":.<20}{prod.name}\n'
                          f'{"Price":.<20}{prod.price}\n'
                          f'{"Amount":.<20}{prod.amount}\n'
                          f'{"Added on":.<20}{prod.add_date}\n'
                          f'{"Description:":<20}\n{prod.description}\n\n'
                          )
            self.stdout.write(out_string)
        else:
            self.stdout.write('Not Found.')
