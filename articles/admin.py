# django imports
from django.contrib import admin

# project imports

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """
    This class handles admin panel for Article model
    """
    list_display = ['id', 'title', 'author']
    list_display_links = ['id']
    search_fields = ['title', 'author', 'description', 'category', 'content']
    list_filter = ['published_at', 'source__name', 'country', 'category', 'author']
    autocomplete_fields = ['source']

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
