from django.contrib import admin
from .models import Article, Student


@admin.register(Article)
class ArticleAdmina(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'birthday', 'age')
