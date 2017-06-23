from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Article

urlpatterns = [
	url(r'^$', ListView.as_view(queryset=Article.objects.all().order_by('-go_live')[:3], template_name='blog/article_list.html')),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Article, template_name='blog/article.html'))
]