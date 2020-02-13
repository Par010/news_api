# rest framework import

from rest_framework.serializers import (
    ModelSerializer,
)

# project level imports

from publishers.models import Publisher


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = [
            'id',
            'name',
            'description'
        ]
