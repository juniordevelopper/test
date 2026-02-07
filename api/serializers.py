from rest_framework import serializers
from posts.models import Post
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    token['firstname'] = user.first_name        
    token['username'] = user.username        
    return token

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