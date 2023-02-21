from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class RequestUserPagination(PageNumberPagination):
    page_size = 5

    def get_paginated_response(self, data):
        return Response(data)
