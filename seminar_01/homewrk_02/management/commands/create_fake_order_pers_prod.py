from django.core.management.base import BaseCommand
from random import sample, randint as rin, choice

from homewrk_02.models import Order, Customer, Product


class Command(BaseCommand):
    help = "Generate some fake orders for person by id."

    def add_arguments(self, parser):
        parser.add_argument('c_pk', type=int, help='Customer ID.')
        parser.add_argument('p_pk', type=int, help='Product ID.')
        parser.add_argument('ulim', type=int, help='Upper limit for amount of orders per person.')

    def handle(self, *args, **options):
        c_pk = options.get('c_pk')
        p_pk = options.get('p_pk')
        ulim = Product.objects.count()
        ulim = options.get('ulim') if options.get('ulim') < (ulim // 10) else 10

        person = Customer.objects.filter(pk=c_pk).first()
        product = Product.objects.filter(pk=p_pk).first()
        total_price = 0
        # prod_set = sample(list(products), rin(1, ulim))
        for _ in range(ulim):
            total_price += product.price
        order_tmp = Order(
            customer=person,
            total_price=total_price,
        )
        order_tmp.save()
        for _ in range(ulim):
            order_tmp.product.add(product)
        order_tmp.save()
