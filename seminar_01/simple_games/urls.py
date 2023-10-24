from django.urls import path
from . import views


urlpatterns = [
    path('simple_games/', views.games_index, name='index'),
    path('simple_games/coinplay/', views.coin, name='coinplay'),
    path('simple_games/diceplay/', views.dice, name='diceplay'),
    path('simple_games/randomizer/', views.random_number, name='random_number'),
    path('simple_games/coinplay_records/<int:amount>/', views.coin_records, name='coinplay_records'),
    path('get_a_game/', views.simple_games_form, name='simple_games_form'),
]
