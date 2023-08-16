from django.shortcuts import render, get_object_or_404
from datetime import datetime as dt, timedelta

from .forms import EditProductForm, AddProductPhoto

from .models import Customer, Product, Order


def products_list(request):
    products = [*enumerate(Product.objects.all().order_by('pk'), start=1)]
    return render(request,
                  'homewrk_02/hw02_products.html',
                  {'title': 'Product list', 'products': products}
                  )


def order_list(request, customer_id):
    """
    List of orders for customer with lists of products
    :param request:
    :param customer_id: int     -- customer id
    :return:
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    context = {
        'title': 'Order list',
        'customer': customer,
    }
    if orders:
        context['orders'] = []
        for order in orders:
            context['orders'].append(
                {
                    'order': order,
                    'products': [item for item in order.product.all()],
                }
            )
    return render(request, 'homewrk_02/hw02_orders.html', context=context)


def ordered_products_list(request, customer_id, period):
    """
    Show products list form orders for defined period
    :param request:
    :param customer_id: int
    :param period: str      -- 'week', 'month' or 'year'
    :return:
    """
    customer = get_object_or_404(Customer, pk=customer_id)

    limit = 7 if period == 'week' else 30 if period == 'month' else 365 if period == 'year' else 0

    date_low_lim = (dt.now() - timedelta(limit + 1)).strftime("%Y-%m-%d")
    print(date_low_lim)
    if not limit:
        orders = Order.objects.filter(customer=customer).order_by('-order_date')
    else:
        orders = Order.objects.filter(customer=customer).filter(order_date__gt=date_low_lim).order_by('pk')
    context = {
        'title': 'Ordered product list for customer',
        'customer': customer, }
    if orders:
        context['products'] = []
        for order in orders:
            context['products'].extend(
                [
                    {
                        'pk': item.pk,
                        'name': item.name,
                        'price': item.price,
                        'date': order.order_date,
                    }
                    for item in order.product.all()
                ]
            )
    return render(request, 'homewrk_02/hw02_ordered_products.html', context=context)


def ordered_products_unique(request, customer_id, period):
    """
    Show non-repeated products list form orders for defined period
    :param request:
    :param customer_id: int
    :param period: str      -- 'week', 'month' or 'year'
    :return:
    """
    customer = get_object_or_404(Customer, pk=customer_id)

    limit = 7 if period == 'week' else 30 if period == 'month' else 365 if period == 'year' else 0

    date_low_lim = (dt.now() - timedelta(limit + 1)).strftime("%Y-%m-%d")
    print(date_low_lim)
    if not limit:
        orders = Order.objects.filter(customer=customer).order_by('-order_date')
    else:
        orders = Order.objects.filter(customer=customer).filter(order_date__gt=date_low_lim).order_by('-order_date')
    context = {
        'title': 'Ordered product list for customer (non-repeating)',
        'customer': customer,
    }
    if orders:
        products_total = set()
        for order in orders:
            products_total.update([*order.product.all()])
        context['products'] = [
            {
                'pk': item.pk,
                'name': item.name,
                'price': item.price,
            }
            for item in sorted(products_total, key=lambda x: x.price)
        ]
    return render(request, 'homewrk_02/hw02_ordered_products_unique.html', context=context)


def edit_product(request):
    """Edit product"""
    if request.method == 'POST':
        form = EditProductForm(request.POST)
        if form.is_valid():
            product_pk = int(form.cleaned_data['product'])
            product = get_object_or_404(Product, pk=product_pk)
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.amount = form.cleaned_data['amount']
            product.add_date = dt.today
            product.save()
    else:
        form = EditProductForm()
    return render(request,
                  'homewrk_02/sm02_edit_products.html',
                  {'title': 'Edit products', 'form': form}
                  )


def add_product_photo(request):
    """Add product photo"""
    if request.method == 'POST':
        print(f'{request.POST=}')

        form = AddProductPhoto(request.POST, request.FILES)
        if form.is_valid():
            print(f'{request.POST=}')
            product_pk = int(form.cleaned_data['product'])
            product = get_object_or_404(Product, pk=product_pk)
            product.p_image = form.cleaned_data['p_image']
            product.save()
    else:
        form = AddProductPhoto()
    return render(request,
                  'homewrk_02/sm02_edit_products.html',
                  {'title': 'Add product photo', 'form': form, }
                  )

