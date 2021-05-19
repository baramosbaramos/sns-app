from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import CommentForm
from .models import CommentModel, Profile
from django.db.models import Q


from django.db import IntegrityError
# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        icon = request.FILES['icon']
        try:
            user = User.objects.create_user(username, '', password)
            user.profile.image = icon
            user.save()
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'this user has already been registered.'})
    else:
        return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Sorry, login failed.'})
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def homefunc(request):
    user = request.user
    users = User.objects.exclude(username=user.username)
    return render(request, 'home.html', {'user':user, 'users':users})

def roomfunc(request, id):
    if request.method == 'POST':
            com = CommentModel()
            com.content = request.POST.get('content')
            com.sender = request.POST.get('sender')
            com.receiver = request.POST.get('receiver')
            if 'image' in request.FILES:
                com.image = request.FILES['image']
            else:
                com.image = ''
            com.save()
    
    user = request.user
    partner = get_object_or_404(User, pk=id)
    comments = CommentModel.objects.filter(Q(sender=user.username, receiver=partner.username) | Q(sender=partner.username, receiver=user.username))
    return render(request, 'room.html', {'user':user, 'partner': partner, 'form': CommentForm(), 'comments': comments})

def commentfunc(CreateView):
    com = CommnetModel()