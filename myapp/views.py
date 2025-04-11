from rest_framework import viewsets
from .models import Post,Comment
from .serializer import PostSerializer,CommentSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer