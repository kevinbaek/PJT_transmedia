import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm

def blog_list(request):
    qs = Post.objects.all()
    return render(request, 'blog/main.html', {
        'post_list': qs,
        })

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    qs = Post.objects.all()
    return render(request, 'blog/detail.html', {
        'post' : post,
        'post_list': qs,
        })
def profile(request):
    qs = Post.objects.all()
    return render(request, 'blog/profile.html', {
        'post_list': qs,
        })

def crawler_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return render(request, 'blog/crawler.html', {
                'form': form,
            })
    else:       
    # if request.method == 'GET':
        form = PostForm()

    return render(request, 'blog/crawler.html', {
        'form': form,
    })