from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import FollowViewSet, GroupViewSet, PostViewSet

api_router = DefaultRouter()
api_router.register('follow', FollowViewSet)
api_router.register('groups', GroupViewSet)
api_router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(api_router.urls)),
]
