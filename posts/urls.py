from django.urls import path
from .views import *

urlpatterns = [
  path('', posts, name='posts'),
  path('post/<int:id>/', post, name='post'),
  path('post/update/<int:id>', post_update, name='post_update'),
  path('post/delete/<int:id>', post_delete, name='post_delete'),
  path('post/create', post_create, name='post_create'),
]