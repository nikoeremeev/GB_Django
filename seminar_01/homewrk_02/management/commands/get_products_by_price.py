from django.core.management.base import BaseCommand
from homewrk_02.models import Product


class Command(BaseCommand):
    help = "Get product(s) by price or a set of products of nearest (lower or above) price."

    def add_arguments(self, parser):
        parser.add_argument('--price', type=float, help='Searched product cost or limit of cost')
        parser.add_argument('--amount', type=int, help='Amount of products to show')
        parser.add_argument('--cheaper', action='store_true', help='Search for cheaper products')
        parser.add_argument('--expensive', action='store_true', help='Search for more expensive products')

    def handle(self, *args, **options):
        products = []
        price = options.get('price')
        if options.get('cheaper'):
            products = Product.objects.order_by('price').filter(price__lt=price).all()
            if amt := options.get('amount'):
                products = products[len(products) - amt:]
        elif options.get('expensive'):
            products = Product.objects.order_by('price').filter(price__gt=price).all()
            if amt := options.get('amount'):
                products = products[:amt]
        else:
            products = Product.objects.filter(price=price).all()
            if amt := options.get('amount'):
                products = products[:amt]

        if products:
            for prod in products:
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
            self.stdout.write('Not found')
