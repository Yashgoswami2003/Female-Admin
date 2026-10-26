from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Blog

def index(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'store/index.html', {'blogs': blogs})

def custom_admin_login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        
        user = authenticate(request, username=u_name, password=pass_word)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin/')
        else:
            messages.error(request, 'Invalid Username or Password!')
            
    return render(request, 'store/login.html')