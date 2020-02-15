# rest framework imports
from rest_framework import routers

# project level imports
from articles.api.views import (
    ArticleViewSet,
)


router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
