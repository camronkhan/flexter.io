from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from blog.models import Article

def find_articles(request):
	# get article list
	articles = Article.objects.all().order_by('-go_live')
	# get query params from url
	page = request.GET.get('page')
	# get paginated list of articles
	paginated_article_list = get_paginated_article_list(articles, page)
	# render result
	return render(request, 'blog/article_list.html', { 'paginated_article_list': paginated_article_list })


def find_articles_via_search(request):
    # get article list
	articles = Article.objects.all().order_by('-go_live')
	# get query params
	term = request.GET.get('term')
	page = request.GET.get('page')
	# filter via search term
	if term:
		articles = articles.filter(Q(title__icontains=term) | Q(summary__icontains=term)).distinct()
		query_param_page = '&term=' + term
	else:
		query_param_page = None
	# get paginated list of articles
	paginated_article_list = get_paginated_article_list(articles, page)
	# create context to pass template
	template_context_dict = { 'paginated_article_list': paginated_article_list }
	if query_param_page:
		template_context_dict['query_param_page'] = query_param_page
	# render result
	return render(request, 'blog/article_list.html', template_context_dict)


def find_articles_via_tag(request):
	# get article list
	articles = Article.objects.all().order_by('-go_live')
	# get query params from url
	tag_id = request.GET.get('id')
	page = request.GET.get('page')
	# filter via tag id
	if tag_id:
		articles = articles.filter(tags__id=tag_id).distinct()
		query_param_page = '&id=' + tag_id	
	else:
		query_param_page = None
	# get paginated list of articles
	paginated_article_list = get_paginated_article_list(articles, page)
	# create context to pass to template
	template_context_dict = { 'paginated_article_list': paginated_article_list }
	if query_param_page:
		template_context_dict['query_param_page'] = query_param_page
	# render result
	return render(request, 'blog/article_list.html', template_context_dict)


def get_paginated_article_list(article_list, page_num):
	page_query_param_name = 'page'
	articles_per_page = 5
	# get paginator with max num articles
	paginator = Paginator(article_list, articles_per_page)
	# if no page exists, use page == 1
	try:
		paginated_article_list = paginator.page(page_num)
	except PageNotAnInteger:
		paginated_article_list = paginator.page(1)
	except EmptyPage:
		paginated_article_list = paginator.page(paginator.num_pages)
	return paginated_article_list