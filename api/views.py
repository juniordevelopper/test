from django.shortcuts import render
from posts.models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_api(request):
  if request.method == 'GET':
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
@permission_classes([IsOwnerOrReadOnly])
def post_id_api(request, id):
  post = Post.objects.get(id=id)
  serializer = PostSerializer(post, many=True)
  return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsOwnerOrReadOnly])
def post_delete_api(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return Response(status=204)

@api_view(['PUT'])
@permission_classes([IsOwnerOrReadOnly])
def post_update_api(request, id):
  post = Post.objects.get(id=id)
  serializer = PostSerializer(post, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=400)