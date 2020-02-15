# rest framework imports
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters import rest_framework as filters


# project level imports

from .serializers import ArticleSerializer
from .pagination import Pagination
from articles.models import Article


class ArticleFilter(filters.FilterSet):
    """
    This class handles Filtering for Article model
    """
    published_at_gte = filters.DateTimeFilter(field_name="published_at", lookup_expr='gte')
    published_at_lte = filters.DateTimeFilter(field_name="published_at", lookup_expr='lte')

    class Meta:
        model = Article
        fields = ['country', 'category', 'author', 'title', 'published_at_gte', 'published_at_lte', 'source__name']


class ArticleViewSet(ReadOnlyModelViewSet):
    """
    This class handles view for Article model. This is a read-only view.
    """
    serializer_class = ArticleSerializer
    pagination_class = Pagination
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['category', 'author', 'title', 'description', 'content']
    ordering = ['title']
    filterset_class = ArticleFilter
    queryset = Article.objects.all()
