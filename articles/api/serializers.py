# rest framework imports

from rest_framework.serializers import (
    ModelSerializer,
    ReadOnlyField
)

# project imports

from publishers.api.serializers import PublisherSerializer
from articles.models import Article


class ArticleSerializer(ModelSerializer):
    """
    This class handles serializer for Article model
    """
    source = PublisherSerializer(many=False, read_only=True)
    urlToImage = ReadOnlyField(source='url_to_image')

    class Meta:
        model = Article
        fields = [
            'source',
            'author',
            'title',
            'description',
            'url',
            'urlToImage',
            'published_at',
            'content'
        ]

