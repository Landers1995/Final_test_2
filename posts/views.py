from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsAdmin, IsOwner
from posts.serializer import PostSerializer, CommentSerializer
from posts.models import Post, Comment


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = serializer.save()
        post.author = self.request.user
        post.save()


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
   #pagination_class = ElectronicNetworksPaginator


class PostRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAdmin | IsOwner]


class PostDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAdmin | IsOwner]


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        comment = serializer.save()
        comment.author = self.request.user
        comment.save()


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny]


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdmin | IsOwner]


class CommentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdmin | IsOwner]
