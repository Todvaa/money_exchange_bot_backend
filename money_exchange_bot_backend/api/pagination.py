from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class RequestUserPagination(PageNumberPagination):
    """Pagination for user's exchange requests"""
    page_size = 5

    def get_paginated_response(self, data):
        return Response(data)
