from posts.apps import PostsConfig
from django.urls import path

from posts.views import PostCreateAPIView, PostListAPIView, PostRetrieveAPIView, \
    PostUpdateAPIView, PostDestroyAPIView, CommentCreateAPIView, CommentListAPIView, \
    CommentRetrieveAPIView, CommentUpdateAPIView, CommentDestroyAPIView

app_name = PostsConfig.name

urlpatterns = [
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostRetrieveAPIView.as_view(), name='post-retrieve'),
    path('post/update/<int:pk>/', PostUpdateAPIView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDestroyAPIView.as_view(), name='post-destroy'),

    path('comment/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comment/', CommentListAPIView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment-retrieve'),
    path('comment/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='comment-update'),
    path('comment/delete/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment-destroy'),
]
