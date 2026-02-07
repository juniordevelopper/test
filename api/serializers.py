from rest_framework import serializers
from posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
  # author = UserSerializer()

  class Meta:
    model = Post
    fields = '__all__'
    # depth = 1