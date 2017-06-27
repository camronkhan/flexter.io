from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from blog.models import Article

def find_articles_via_search(request):
	queryset = Article.objects.all().order_by('-go_live')
	query = request.GET.get('q')

	if query:
		queryset = queryset.filter(
				Q(title__icontains=query) |
				Q(summary__icontains=query)
			).distinct()

	context = { 'object_list': queryset }

	return render(request, 'blog/article_list.html', context)


def find_articles_via_tag(request):
	queryset = Article.objects.all().order_by('-go_live')
	query = request.GET.get('id')

	if query:
		queryset = queryset.filter(tags__id=query).distinct()

	context = { 'object_list': queryset }

	return render(request, 'blog/article_list.html', context)

