from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('articles/<int:author_id>/', views.articles, name='articles'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
]
