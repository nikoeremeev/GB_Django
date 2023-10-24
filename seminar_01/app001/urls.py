from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('author_articles/<int:author_id>/', views.get_articles, name='get_articles'),
    path('get_article/<int:article_id>/', views.add_commentary_form_simple, name='add_commentary_form_simple'),
    path('add_author/', views.add_author_form, name='add_author_form'),
    path('add_article/', views.add_article, name='add_article'),
]
