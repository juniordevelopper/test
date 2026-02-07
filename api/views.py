from posts.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['author', 'title']
  search_fields = ['title', 'author__username']
  ordering_fields = ['username', 'created_at']
