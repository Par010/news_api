# django imports
from django.db import models

# project imports
from articles.utils.constants import COUNTRY_OPTIONS, AUSTRALIA, CATEGORY_OPTIONS
from publishers.models import Publisher

# Create your models here.


class Article(models.Model):
    source = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True,
                               related_name='article_to_publisher')
    country = models.CharField(max_length=2, default=AUSTRALIA, choices=COUNTRY_OPTIONS)
    category = models.CharField(max_length=2, blank=True, null=True, choices=CATEGORY_OPTIONS)
    author = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=400, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    url_to_image = models.URLField(max_length=500, null=True, blank=True, verbose_name="urlToImage")
    published_at = models.DateTimeField(null=True, blank=True, auto_now_add=False, auto_now=False,
                                        verbose_name="publishedAt")
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title






