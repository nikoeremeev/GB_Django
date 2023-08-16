from django.core.management.base import BaseCommand
from random import sample, randint as rin, choice

from homewrk_02.models import Order, Customer, Product


class Command(BaseCommand):
    help = "Generate some fake orders."

    def handle(self, *args, **options):
        result_string = ''
        orders = Order.objects.all()
        if not orders:
            self.stdout.write("No orders found.")
            return

        for order in orders:
            result_string += str(order) + '\n\nProducts:\n'
            result_string += ('~' * 10) + '\n'
            result_string += '\n'.join([str(item) for item in order.product.all()])
            result_string += '\n' + ('=' * 120) + '\n'
        self.stdout.write(result_string)