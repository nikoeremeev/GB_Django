from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

LINKS = {
    'Add article': 'app001/add_article/',
    'fake shop': 'homework02/products_list/',
    'games': 'games/get_a_game/',
}


def index(request):
    logger.info(f'Index accessed')
    context = {
        "title": "Index page of Homework 06",
        "body": "At this stage just a stub page to demonstrate "
                "the site is able to function.",
        "links": LINKS,
    }
    return render(request, "front/index.html", context=context)


def about(request):
    logger.info(f'About accessed')
    context = {"title": "About page of Homework 06"}
    return render(request, "front/about.html", context=context)
