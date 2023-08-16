from django.core.management.base import BaseCommand
from homewrk_02.models import Order, Customer, Product


class Command(BaseCommand):
    help = "Read orders by customer ID or name."

    def add_arguments(self, parser):
        parser.add_argument('--id', type=int, help='Customer ID')
        parser.add_argument('--name', type=str, help='Customer name')

    def handle(self, *args, **options):
        result_string = ''
        if pk := options.get('id'):
            orders = Order.objects.filter(
                customer=Customer.objects.filter(pk=pk).first()
            ).all()
        elif name := options.get('name'):
            orders = Order.objects.filter(
                customer=Customer.objects.filter(name=name).first()
            ).all()
        else:
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
