from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging

from .models import Author, Article, Commentary

logger = logging.getLogger(__name__)



def index(request):
    logger.info(f'Index accessed')
    context = {"title": "Index page"}
    return render(request, "firstapp/index.html", context=context)


def about(request):
    logger.info(f'About accessed')
    context = {"title": "About page"}
    return render(request, "firstapp/about.html", context=context)


# =========================================================================
# Доработаем задачи из прошлого семинара по созданию моделей автора,
# статьи и комментария.
# Создайте шаблон для вывода всех статей автора в виде списка заголовков.
# Если статья опубликована, заголовок должен быть ссылкой на статью.
# Если не опубликована, без ссылки.
# Не забываем про код представления с запросом к базе данных и маршруты.
# =========================================================================


def articles(request, author_id):
    author = Author.objects.filter(pk=author_id).first()
    context = {
        "author": f'{author.name} {author.surname}',
        "articles": list(Article.objects.filter(author=author))
    }
    return render(request, 'firstapp/authors_records.html', context=context)


# =========================================================================
# Доработаем задачу 4.
# Создай шаблон для вывода подробной информации о статье.
# Внесите изменения в views.py - создайте представление и
# в urls.py - добавьте маршрут.
# *Увеличивайте счётчик просмотра статьи на единицу при каждом просмотре
# =========================================================================


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(Author, pk=article.author.pk)
    commentaries = Commentary.objects.filter(article=article).all()
    context = {
        'article': article,
        'author': author,
        'commentaries': commentaries,
    }
    return render(request, 'firstapp/article.html', context=context)

# =========================================================================
# Измените шаблон для вывода заголовка и текста статьи, а также всех
# комментариев к статье с указанием текста комментария, автора комментария
# и даты обновления комментария в хронологическом порядке.
# Если комментарий изменялся, дополнительно напишите “изменено”.
# Не забывайте про представление с запросом в БД и маршруты. Проверьте, что
# они работают верно
# =========================================================================
