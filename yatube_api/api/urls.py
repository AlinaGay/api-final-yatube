from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

api_router = DefaultRouter()
api_router.register('follow', FollowViewSet, basename='follow')
api_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
api_router.register('groups', GroupViewSet, basename='group')
api_router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(api_router.urls)),
]
