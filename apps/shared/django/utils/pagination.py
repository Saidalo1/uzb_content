from django.core.paginator import Paginator
from django.utils.functional import cached_property
from rest_framework.pagination import PageNumberPagination


class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        # only select 'id' for counting, much cheaper
        return self.object_list.values('id').count()


class ProductPagination(PageNumberPagination):
    django_paginator_class = FasterDjangoPaginator
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
