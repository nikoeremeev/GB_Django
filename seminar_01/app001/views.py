from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging

from .forms import AddAuthorForm, AddCommentary, AddArticle
from .models import Author, Article, Commentary

logger = logging.getLogger(__name__)


def add_author_form(request):
    """Form to add an author"""
    title = "Add author"
    message = 'Wrong input'

    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            Author(
                name=name,
                surname=surname,
                email=email,
                biography=biography,
                birthday=birthday,
            ).save()
            logger.info(f'Added a new author: {name} {surname} {birthday}')
    else:
        message = 'Fill a form to add author, please.'
        form = AddAuthorForm()
    return render(request, 'app001/add_author_form.html',
                  {'form': form, 'title': title, 'message': message})


def add_commentary_form_simple(request, article_id):
    """form to add a commentary by author"""

    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(Author, pk=article.author.pk)
    article.views += 1
    article.save()
    commentaries = Commentary.objects.filter(article=article)
    print(type(commentaries))
    context = {
        'article': article,
        'author': author,
        'commentaries': commentaries,
        'form': AddCommentary(),
        'button': 'Publish',
    }

    if request.method == 'POST':
        form = AddCommentary(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            author_pk = form.cleaned_data['author_pk']
            c_author = get_object_or_404(Author, pk=author_pk)
            c_article = get_object_or_404(Article, pk=article_id)
            Commentary(
                author=c_author,
                article=c_article,
                content=content,
            ).save()

    return render(request, 'app001/article.html', context)


def add_article(request):
    if request.method == 'POST':
        form = AddArticle(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            article = Article(
                title=title,
                content=content,
                author=author,
                category=category,
            )
            article.save()
            logger.info(f'Added article: {article}')
    else:
        logger.info(f'Adding article')
        form = AddArticle()
    return render(request, 'app001/add_article.html',
                  {'form': form, 'title': 'Add article', 'button': 'Add Article'})


# def index_old(request):
#     logger.info(f'Index accessed')
#     html = """<html>
#     <head><title>Index page</title></head>
#     <body>
#     <div><h2>Site Start Page</h2></div>
#         <div>
#             <ul>Simple Games
#                 <li><a href="games">Games Page</a></li>
#             </ul>
#         </div>
#         <footer>
#         <a href="">Main</a>&nbsp;&nbsp;&nbsp;
#         <a href="about/">About</a>
#         </footer>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)
#
#
# def about_old(request):
#     logger.info(f'About accessed')
#     html = """<html>
#     <head><title>About page</title></head>
#     <body>
#     <div><h2>Site About Page</h2></div>
#          <div>
#           <p><strong>Lorem ipsum</strong> dolor sit amet, consectetur adipisicing elit.
#           Ab amet blanditiis dolores laudantium maiores, nulla quas
#           repudiandae saepe. A aspernatur consectetur dolore est illo nam
#           necessitatibus nostrum nulla numquam tempora! Culpa delectus dolorem,
#           dolorum ea eos eveniet facilis fugiat illo illum in ipsum minima
#           neque odit perferendis porro quaerat quia quibusdam quo quod
#           reiciendis repudiandae saepe similique, temporibus vel
#           voluptate. Aut beatae doloremque fugiat laboriosam magni,
#           optio qui quia recusandae ut veritatis. Commodi, culpa dignissimos
#           doloribus est et illo, ipsa laboriosam laborum molestias natus nemo
#           odit officiis placeat sequi sunt veniam, voluptas!
#           At ea ex odit placeat sunt? Assumenda, tenetur!</p>
#         </div>
#         <footer>
#         <a href="/">Main</a>&nbsp;&nbsp;&nbsp;
#         <a href="">About</a>
#         </footer>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)


def index(request):
    logger.info(f'Index accessed')
    context = {"title": "Index page"}
    return render(request, "app001/index.html", context=context)


def about(request):
    logger.info(f'About accessed')
    context = {"title": "About page"}
    return render(request, "app001/about.html", context=context)


def get_articles(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {
        "author": f'{author.name} {author.surname}',
        "articles": Article.objects.filter(author=author),
    }
    return render(request, 'app001/authors_records.html', context=context)


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(Author, pk=article.author.pk)
    article.views += 1
    article.save()
    commentaries = Commentary.objects.filter(article=article).all()
    context = {
        'article': article,
        'author': author,
        'commentaries': commentaries,
    }
    return render(request, 'app001/article.html', context=context)
