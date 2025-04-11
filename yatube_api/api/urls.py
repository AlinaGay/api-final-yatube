from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_api_router = DefaultRouter()
v1_api_router.register('follow', FollowViewSet, basename='follow')
v1_api_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
v1_api_router.register('groups', GroupViewSet, basename='group')
v1_api_router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_api_router.urls)),
]
