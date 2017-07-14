from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from blog.models import Article

articles_per_page = 5

def find_articles_via_search(request):
    # get article list
	articles = Article.objects.all().order_by('-go_live')
	# get 'q' query param from url
	query_param = request.GET.get('q')
	# filter via query param
	if query_param:
		articles = articles.filter(Q(title__icontains=query_param) | Q(summary__icontains=query_param)).distinct()
		pagination_query_param = '&q=' + query_param
	# get 'page' query param from url
	page = request.GET.get('page', 1)
	# get paginator with max num articles
	paginator = Paginator(articles, articles_per_page)
	# if no page exists, use page == 1
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	# render result
	return render(request, 'blog/article_list.html', { 'articles': articles, 'pagination_query_param': pagination_query_param })


def find_articles_via_tag(request):
	# get article list
	articles = Article.objects.all().order_by('-go_live')
	# get 'q' query param from url
	query_param = request.GET.get('id')
	# filter via query param
	if query_param:
		articles = articles.filter(tags__id=query_param).distinct()
		pagination_query_param = '&id=' + query_param
	# get 'page' query param from url
	page = request.GET.get('page', 1)
	# get paginator with max num articles
	paginator = Paginator(articles, articles_per_page)
	# if no page exists, use page == 1
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	# render result
	return render(request, 'blog/article_list.html', {'articles': articles, 'pagination_query_param': pagination_query_param })


def load_article_list(request):
	articles = Article.objects.all().order_by('-go_live')
	page = request.GET.get('page', 1)
	paginator = Paginator(articles, articles_per_page)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_ages)
	return render(request, 'blog/article_list.html', { 'articles': articles })

