from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, filters

from exchange.models import User, Request
from api.serializers import (
    UserSerializer, RequestSerializer, UserAdminSerializer
)
from api.pagination import RequestUserPagination


class CreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class CreateRetrieveListUpdateViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin,
    mixins.ListModelMixin, mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    pass


class RetrieveUpdateListViewSet(
    mixins.UpdateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    pass


class UserViewSet(CreateRetrieveListUpdateViewSet):
    """ViewSet for User with user access"""
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('referrer__id',)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        chat_id = self.request.data['id']
        referrer_id = self.request.data['referrer']
        try:
            referrer = User.objects.get(id=referrer_id)
        except User.DoesNotExist:
            referrer = None
        try:
            serializer.save(referrer=referrer, id=chat_id)
        except IntegrityError:
            pass

    def perform_update(self, serializer):
        if self.request.data['username'] == '0':
            serializer.save(username=None)
        else:
            return super().perform_update(serializer)


class RequestUserViewSet(CreateListViewSet):
    """ViewSet for Request with user access"""
    serializer_class = RequestSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    pagination_class = RequestUserPagination
    ordering_fields = ('creation_date',)
    search_fields = ('status',)

    def get_queryset(self):
        owner_id = self.kwargs.get('owner_id')
        requests = Request.objects.filter(owner_id=owner_id)
        return requests.all()

    def perform_create(self, serializer):
        owner_id = self.kwargs.get('owner_id')
        serializer.save(owner_id=owner_id)


class RequestAdminViewSet(RetrieveUpdateListViewSet):
    """ViewSet for Request with admin access"""
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('status',)
    ordering_fields = ('creation_date',)


class UserAdminViewSet(RetrieveUpdateListViewSet):
    """ViewSet for User with admin access"""
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('role',)
    ordering_fields = ('fee',)

    def get_queryset(self):
        if (
                self.action == 'list' and
                self.request.query_params['search'] != 'banned'
        ):
            users = User.objects.filter(fee__gt=0)
            return users.all()
        else:
            return super().get_queryset()

    def perform_update(self, serializer):
        user = get_object_or_404(User, id=self.kwargs['pk'])
        if 'fee' in self.request.data:
            fee = float(user.fee) + float(self.request.data['fee'])
            serializer.save(fee=fee)
        if 'paid_fee' in self.request.data:
            paid_fee = float(user.paid_fee) + float(self.request.data['paid_fee'])
            fee = float(user.fee) - paid_fee
            serializer.save(fee=fee, paid_fee=paid_fee)
        if 'role' in self.request.data:
            serializer.save(role=self.request.data['role'])
