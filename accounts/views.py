from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
User = get_user_model()

def register_view(request):
  if request.user.is_authenticated:
    return redirect('home')
  
  if request.method == 'POST':
    firstname = request.POST.get('firstname').strip()
    lastname = request.POST.get('lastname').strip()
    username = request.POST.get('username').strip()
    email = request.POST.get('email').strip()
    password = request.POST.get('password').strip()
    phone = request.POST.get('phone').strip()

    if User.objects.filter(username=username).exists():
      messages.error(request, 'Username already exists!')
      return redirect('register')
    
    user = User.objects.create_user(
      first_name = firstname,
      last_name = lastname,
      username = username,
      email = email,
      password = password,
      phone = phone
    )
    messages.success(request, f"Siz Shaxsiy kabinet yaratdingiz! Endi shaxsiy accountingizga kirishingiz mumkin!")
    return redirect('login')
  
  return render(request, 'auth/register.html')

def login_view(request):
  if request.user.is_authenticated:
    return redirect('home')

  if request.method == 'POST':
    username = request.POST.get('username').strip()
    password = request.POST.get('password').strip()

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, f"Siz tizimga kirdingiz!")
      return redirect('home')
    messages.error(request, f"Username yoki parol xato!")
  return render(request, 'auth/login.html')

@login_required
def home_view(request):
  return redirect('posts')

def logout_view(request):
  logout(request)
  return redirect('home')