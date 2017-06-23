from django.contrib import admin
from blog.models import Article, Tag, LinkType, Link

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(LinkType)
admin.site.register(Link)