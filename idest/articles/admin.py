from django.contrib import admin
from articles.models import ArticlePost,Comment

# Register your models here.

admin.site.register(ArticlePost)
admin.site.register(Comment)