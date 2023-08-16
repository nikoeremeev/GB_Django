from django import forms

from .models import Product


class EditProductForm(forms.Form):
    products = [(f'{product.pk}', f'id: {product.pk} name: {product.name} price: {product.price}')
                for product in Product.objects.all()]
    product = forms.ChoiceField(choices=products)
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    amount = forms.IntegerField(min_value=0)
    description = forms.CharField(
        max_length=300,
        widget=forms.Textarea()
    )


class AddProductPhoto(forms.Form):
    products = [(f'{product.pk}', f'id: {product.pk} name: {product.name} price: {product.price}')
                for product in Product.objects.all()]
    product = forms.ChoiceField(choices=products)
    p_image = forms.ImageField()
