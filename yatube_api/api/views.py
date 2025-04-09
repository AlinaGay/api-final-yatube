from rest_framework import mixins, viewsets

from posts.models import Group, Post, User
from .serializers import (
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(CreateListViewSet):
    queryset = User.objects.all()
    serializer_class = FollowSerializer
