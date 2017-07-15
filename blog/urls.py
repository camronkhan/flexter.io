from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Article
from blog.views import find_articles, find_articles_via_search, find_articles_via_tag

urlpatterns = [
	url(r'^$', find_articles, name='blog'),
	url(r'^search/$', find_articles_via_search, name='search'),
	url(r'^tag/$', find_articles_via_tag, name='tag'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Article, template_name='blog/article.html'))	
]