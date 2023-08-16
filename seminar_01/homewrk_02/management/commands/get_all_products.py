from django.core.management.base import BaseCommand
from hw_app.models import Product


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **options):
        for prod in Product.objects.all():
            out_string = ('=' * 80 +
                          f'\n{"Product id:":.<20}{prod.pk}\n'
                          f'{"Name":.<20}{prod.name}\n'
                          f'{"Price":.<20}{prod.price}\n'
                          f'{"Amount":.<20}{prod.amount}\n'
                          f'{"Added on":.<20}{prod.add_date}\n'
                          f'{"Description:":<20}\n{prod.description}\n\n'
                          )
            self.stdout.write(out_string)