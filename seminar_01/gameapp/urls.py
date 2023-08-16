from django.urls import path
from . import views
urlpatterns = {
    path('', views.index, name='index'),
    path('coinplay/', views.coin, name='coinplay'),
    path('diceplay/', views.dice, name='diceplay'),
    path('randomizer/', views.random_number, name='random_number'),
    path('coinplay_records/<int:amount>/', views.coin_records, name='coinplay_records'),
    path('diceplay_records/<int:amount>', views.dice_records, name='diceplay_records'),
    path('randomizer_records/<int:amount>', views.random_number_records, name='random_number_records'),
}