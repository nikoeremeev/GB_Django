from django.core.management.base import BaseCommand
from homewrk_02.models import Customer


class Command(BaseCommand):
    help = "Get all customers."

    def handle(self, *args, **options):
        for person in Customer.objects.all():
            out_string = ('=' * 80 +
                          f'\n{"id:":.<20}{person.pk}\n'
                          f'{"name":.<20}{person.name}\n'
                          f'{"email":.<20}{person.email}\n'
                          f'{"address":.<20}{person.address}\n'
                          f'{"registration date":.<20}{person.reg_date}\n\n')
            self.stdout.write(out_string)
