from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    UserViewSet, RequestUserViewSet, RequestAdminViewSet, UserAdminViewSet
)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'user', UserViewSet, basename='user')
router_v1.register(r'(?P<owner_id>\d+)/request-user', RequestUserViewSet, basename='request-user')
router_v1.register(r'request-admin', RequestAdminViewSet, basename='request-admin')
router_v1.register(r'user-admin', UserAdminViewSet, basename='user-admin')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
