from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Profile, UserComment
from .forms import CommentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password


@login_required
def delete_profile(request):
    if request.method == 'POST':
        # Kullanıcıyı silme işlemi
        user = request.user
        user.delete()
        # Oturumu sonlandır ve ana sayfaya yönlendir
        return redirect('index')
    else:
        return redirect('index')  # POST dışındaki talepleri reddet

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('profile_detail')

@login_required
def created_blogs(request):
    user = request.user
    created_blogs = Post.objects.filter(author=user)
    return render(request, 'created_blogs.html', {'created_blogs': created_blogs})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            user = request.user
            UserComment.objects.create(user=user, content=content)
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def profile_edit(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        new_email = request.POST.get('email')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')

        request.user.email = new_email
        request.user.save()

        profile.first_name = new_first_name
        profile.last_name = new_last_name
        profile.save()

        messages.success(request, 'Profil bilgileriniz başarıyla güncellendi.')
        return redirect('profile_detail')

    return render(request, 'profile_edit.html', {'profile': profile})

@login_required
def profile_detail(request):
    user = request.user
    return render(request, 'profile_detail.html', {'user': user})

@login_required
def PostView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        content = request.POST.get('content')
        post.comments.create(content=content)
        return redirect('blog_detail', post_id=post_id)
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments})

def blog_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        content = request.POST.get('content')
        post.comments.create(content=content)
        return redirect('blog_detail', post_id=post_id)
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_name = request.POST.get('author_name')
        file = request.FILES.get('file')
        user, created = User.objects.get_or_create(username=author_name)
        post = Post.objects.create(title=title, content=content, author=user, file=file)
        return redirect('home')
    else:
        return render(request, 'create_post.html')

@login_required
def blog_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        post = Post.objects.create(title=title, content=content, author=author)
        return redirect('home')
    return render(request, 'blog_post.html')

@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        
        return redirect('index')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            error_message = "Kullanıcı adı veya şifre hatalı."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

from django.http import JsonResponse

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True
    like_count = post.likes.count()
    return JsonResponse({'liked': liked, 'like_count': like_count})