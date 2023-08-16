from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:customer_id>/', views.order_list, name='orders_list'),
    path('ordered_products/<int:customer_id>/<slug:period>/', views.ordered_products_list, name='ordered_products'),
    path('ordered_products_unique/<int:customer_id>/<slug:period>/',
         views.ordered_products_unique,
         name='ordered_products_unique'),
]
