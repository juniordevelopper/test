from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def posts(request):
  posts = Post.objects.all()
  return render(request, 'posts.html', {'posts': posts})

@login_required
def post(request, id):
  post = get_object_or_404(Post, id=id)
  print(post)
  return render(request, 'post.html', {'post': post})

@login_required
def post_update(request, id):
  post = get_object_or_404(Post, id=id)

  if request.method == 'POST':
    if not post:
      messages.error(request, 'Post Mavjud emas!')
      return redirect('post', id=id)
    else:
      if post.author != request.user:
        messages.error(request, 'Siz postni tahrirlay olmaysiz!')
        return redirect('post', id=id)
      else:
        title = request.POST.get('title').strip()
        body = request.POST.get('body').strip()
        post.title = title
        post.body = body
        post.save()
        messages.success(request, 'Post muvaffaqqiyatli tahrirlandi!')
        return redirect('post', id=id)
  return render(request, 'post_update.html', {'post': post})

@login_required      
def post_delete(request, id):
  post  = get_object_or_404(Post, id=id)

  if not post:
    messages.error(request, 'Post Mavjud emas!')
    return redirect('post', id=id)
  else:
    if post.author != request.user:
      messages.error(request, 'Siz postni o\'chira olmaysiz!')
      return redirect('post', id=id)
    else:
      post.delete()
      messages.success(request, 'Post muvaffaqqiyatli o\'chirildi!')
      return redirect('posts')

@login_required    
def post_create(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    body = request.POST.get('body')
    post = Post.objects.create(
      author = request.user,
      title = title,
      body = body
    )
    messages.success(request, f"Post muvaffaqiyatli yaratildi!")
    return redirect('post', id=post.id)
  return render(request, 'post_create.html')