from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework import mixins
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Group, Post
from .permission import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class GetOrCreateViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    '''Parrent class for GET and POST methods'''
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(GetOrCreateViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    search_fields = ['user__username']

    def perform_create(self, serializer):
        serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        queryset = post.comments.all()
        return queryset


class FollowViewSet(GetOrCreateViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.following.all()
