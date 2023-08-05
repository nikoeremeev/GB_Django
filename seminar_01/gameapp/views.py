from django.shortcuts import render

import random
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page for GAMES accessed')
    return HttpResponse("<head><title>Games</title></head>" \
                        "<body>" \
                        "<a href='/'>Главная</a><br>" \
                        "<a href='/games'>Игры</a><br>" \
                        "<a href='/'>Обо мне</a><br>" \
                        "<h1>Выберете что хотите получить:</h1><br>" \
                        "<a href='/games/coin'>Орёл или решка</a><br>" \
                        "<a href='/games/dice'>Игральная кость</a><br>" \
                        "<a href='/games/rndnumber'>Случайное число от 0 до 100</a><br>" \
                        "</body>")


def coin(request):
    word = random.choice(["орел", "решка"])
    logger.info(f'Coin play page accessed. Answer: {word}')
    return HttpResponse(f"Итог:  {word}")


def dice(request):
    number = random.randint(1, 6)
    logger.info(f'Dice play page accessed. Answer: {number}')
    return HttpResponse(f"На кубике выпала грань:  {number}")


def rndnumber(request):
    number = random.randint(0, 100)
    logger.info(f'Random number play page accessed. Answer: {number}')
    return HttpResponse(f"Случаное число:  {number}")
