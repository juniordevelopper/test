from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()
def site_stats(request):
  total_users = User.objects.count()
  total_posts = Post.objects.count()
  return {
    'total_users': total_users,
    'total_posts': total_posts
  }