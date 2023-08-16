from django.contrib import admin
from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    ordering = ('name', 'email', 'address')
    list_filter = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ['reg_date', 'reg_date']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email', 'phone'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'fields': ['address', 'reg_date']
            },
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    ordering = ('name', 'price', 'amount')
    list_filter = ('name', 'price', 'amount')
    readonly_fields = ('add_date', 'p_image')

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'price', 'amount'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'fields': ['add_date', 'p_image']
            },
        ),
        (
            'Description',
            {
                'classes': ['collapse'],
                'fields': ['description']
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    fields = ['customer', 'product', 'total_price', 'order_date']
    ordering = ('customer', 'product', '-total_price')
    list_filter = ('customer', 'order_date', 'total_price', 'product',)
    search_fields = ('customer', 'product', 'order_date')
    readonly_fields = ('order_date', 'total_price', 'customer', 'product')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
