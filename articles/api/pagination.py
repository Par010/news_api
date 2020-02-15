# rest framework imports
from rest_framework.pagination import (
    PageNumberPagination
)


class Pagination(PageNumberPagination):
    """
    This class handles the pagination for resources
    """
    page_size_query_param = 'pageSize'
    page_size = 10
