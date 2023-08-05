from django.shortcuts import render

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    HTML_block = "<head><title>Главная</title></head>" \
                 "<body>" \
                 "<a href='/'>Главная</a><br>" \
                 "<a href='/games'>Игры</a><br>" \
                 "<a href='/about'>Обо мне</a><br>" \
                 "</body>"
    return HttpResponse(HTML_block)

def about(request):
    logger.info('About page accessed')
    HTML_block = "<head><title>Обо мне</title></head>" \
                 "<body>" \
                 "<a href='/'>Главная</a><br>" \
                 "<a href='/games'>Игры</a><br>" \
                 "<a href='/'>Обо мне</a><br>" \
                "<h1>Обо мне</h1><br>"\
                "<p>Я, Еремеев Николай.</p>" \
                 "<a href='https://github.com/nikoeremeev/GB_Django'>Ссылка на мой репозиторий</a><br>" \
                 "</body>"
    return HttpResponse(HTML_block)