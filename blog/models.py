from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
	content = models.CharField(max_length=50, unique=True, null=False)
	use_count = models.PositiveIntegerField(default=0, editable=False, null=False)
	articles = models.ManyToManyField('Article', blank=True)
	
	def __str__(self):
		return self.content


class LinkType(models.Model):
	name = models.CharField(max_length=100, unique=True, null=False)

	def __str__(self):
		return self.content


class Article(models.Model):
	title = models.CharField(max_length=100, null=False)
	summary = models.CharField(max_length=300, null=False)
	content = models.TextField(null=False)
	author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, through=Tag.articles.through, blank=True)
	go_live = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.title


class Link(models.Model):
	url = models.CharField(max_length=3000, null=False)
	article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)
	link_type = models.ForeignKey(LinkType, null=False, on_delete=models.CASCADE)

	def __str__(self):
		return self.url
