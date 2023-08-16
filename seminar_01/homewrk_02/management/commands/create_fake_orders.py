from django.core.management.base import BaseCommand
from random import sample, randint as rin, choice

from homewrk_02.models import Order, Customer, Product


class Command(BaseCommand):
    help = "Generate some fake orders."

    def add_arguments(self, parser):
        parser.add_argument('amt', type=int, help='Amount of persons ordered something.')
        parser.add_argument('ulim', type=int, help='Upper limit for amount of orders per person.')

    def handle(self, *args, **options):
        amt = Customer.objects.count()
        amt = options.get('amt') if options.get('amt') < amt else amt
        ulim = Product.objects.count()
        ulim = options.get('ulim') if options.get('ulim') < (ulim // 10) else 10

        persons = sample(list(Customer.objects.all()), amt)
        products = Product.objects.all()
        for pers in persons:
            total_price = 0
            prod_set = sample(list(products), rin(1, ulim))
            for prod in prod_set:
                total_price += prod.price
            order_tmp = Order(
                customer=pers,
                total_price=total_price,
            )
            order_tmp.save()
            for prod in prod_set:
                order_tmp.product.add(prod)
            order_tmp.save()
