from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Article
from blog.views import find_articles_via_search, find_articles_via_tag, load_article_list

urlpatterns = [
	#url(r'^$', ListView.as_view(queryset=Article.objects.all().order_by('-go_live')[:10], template_name='blog/article_list.html')),
	url(r'^$', load_article_list, name = 'blog'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Article, template_name='blog/article.html')),
	url(r'^search/$', find_articles_via_search, name='search'),
	url(r'^tag/$', find_articles_via_tag, name='tag')
]