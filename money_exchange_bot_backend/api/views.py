from django.db import IntegrityError
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from exchange.models import User, Request
from api.serializers import (
    UserSerializer, RequestSerializer, UserAdminSerializer
)
from api.pagination import RequestUserPagination


class ListViewSet(
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class CreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class CreateRetrieveListViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin,
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class UpdateListViewSet(
    mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class UserViewSet(CreateRetrieveListViewSet):
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('referrer__id',)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        chat_id = self.request.data['id']
        referrer_id = self.request.data['referrer']
        try:
            referrer = User.objects.get(id=referrer_id)
            #todo: send message to referrer
        except User.DoesNotExist:
            referrer = None
        serializer.save(referrer=referrer, id=chat_id)


class RequestUserViewSet(CreateListViewSet):
    serializer_class = RequestSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    pagination_class = RequestUserPagination
    ordering_fields = ('creation_date',)
    search_fields = ('status',)

    def get_queryset(self):
        owner_id = self.kwargs.get("owner_id")
        requests = Request.objects.filter(owner_id=owner_id)
        return requests.all()

    def perform_create(self, serializer):
        owner_id = self.kwargs.get("owner_id")
        serializer.save(owner_id=owner_id)


class RequestAdminViewSet(UpdateListViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('status', 'owner',)
    ordering_fields = ('creation_date',)


class UserAdminViewSet(ListViewSet):
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
