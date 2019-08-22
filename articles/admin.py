from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmina(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
