from django.urls import path
from blog.views import (
    PostListView,
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    )
from blog.views import home , about

app_name = 'blog'
urlpatterns = [
    # path('',home, name='blog-home'),
    path('about/',about, name='blog-about'),

    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),


] 
