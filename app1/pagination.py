from rest_framework.pagination import PageNumberPagination


class First_paginator_class(PageNumberPagination):
    page_size = 5
    page_query_param = 'cart'
    page_size_query_param = 'size'
    # max_page_size = 5
    # last_page_strings = 'end'