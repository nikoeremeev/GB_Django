from django.shortcuts import render
from django.http import HttpResponse
from .models import CoinPlay
from random import randint
import logging

logger = logging.getLogger(__name__)
GAME_HTML = """<html>
        <head><title>{title}</title></head>
        <body>
        <div><h2>{title}</h2</div>
            <div>
            {result}<br><br><br>
            {links}
            </div>
            <footer>
            <a href="/">Main</a>&nbsp;&nbsp;&nbsp;
            <a href="/about">About</a>
            </footer>
        </body>
        </html>
        """


def index(request):
    html = """<html>
    <head><title>Index page</title></head>
    <body>
    <div><h2>Games Index Page</h2</div>
        <div>
            <ul>Simple Games
                <li><a href="coinplay">Coin play</a></li>
                <li><a href="diceplay">Dice play</a></li>
                <li><a href="randomizer">Random number</a></li>
            </ul>
        </div>
        <footer>
        <a href="/">Main</a>&nbsp;&nbsp;&nbsp;
        <a href="/about">About</a>
        </footer>
    </body>
    </html>
    """
    logger.info(f'Games accessed')
    return HttpResponse(html)


def coin(request):
    try:
        side = ('Obverse', 'Reverse')[randint(0, 3)]
        out = GAME_HTML.format(
            title="Coin Play",
            result=f"Coin side: {side}",
            links='<a href="">Again</a><br>'
                  '<a href="/games">Back</a><br>'
        )
    except Exception as exc:
        logger.exception(f'Error occurred: {exc}')
        return HttpResponse(f'Coin has stuck in air<br><br><a href="">Again</a><br><a href="/games">Back</a>')
    else:
        logger.info(f'coinplay requested; coin side: {side}')
        return HttpResponse(out)


def dice(request):
    cube_side = randint(1, 6)
    out = GAME_HTML.format(
        title="Dice Play",
        result=f"Cube Side Value: {cube_side}",
        links='<a href="">Again</a><br>'
              '<a href="/games">Back</a><br>'
    )
    logger.info(f'diceplay requested; cube-side: {cube_side}')
    return HttpResponse(out)


def random_number(request):
    answer = randint(0, 100)
    logger.info(f'random_number requested; answer: {answer}')
    out = GAME_HTML.format(
        title="Random Number",
        result=f"Your number: {answer}",
        links='<a href="">Again</a><br>'
              '<a href="/games">Back</a><br>'
    )
    return HttpResponse(out)


def coin_records(request, amount):
    context = {'game': 'Coin play', 'attempts': []}
    # aggregate = {'obverse': 0, 'reverse': 0}

    for a_throw in list(CoinPlay.objects.all())[-amount:]:
        if a_throw.side == 'obverse':
            context['attempts'].append('obverse')
        else:
            context['attempts'].append('reverse')
    return render(request, 'app001/common_records.html', context=context)


def dice_records(request):
    ...


def random_number_records(request):
    ...
