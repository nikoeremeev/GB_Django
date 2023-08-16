from django.core.management.base import BaseCommand
from homewrk_02.models import Customer


class Command(BaseCommand):
    help = "Get customer by name."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Searched customer name ("name surname")')

    def handle(self, *args, **options):
        name = options.get('name')
        if person := Customer.objects.filter(name=name).first():
            out_string = ('=' * 80 +
                          f'\n{"Customer id:":.<20}{person.id}\n'
                          f'{"Name":.<20}{person.name}\n'
                          f'{"Email":.<20}{person.email}\n'
                          f'{"Address":.<20}{person.address}\n'
                          f'{"Registration date":.<20}{person.reg_date}\n\n')
            self.stdout.write(out_string)
        else:
            self.stdout.write('Not Found.')
