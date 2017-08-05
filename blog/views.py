import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm, EditForm

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

def blog_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':    
        form = EditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:blog_detail', post.id)
    else:
    # if request.method == 'GET':
        form = EditForm(instance=post)

    return render(request, 'blog/crawler.html', {
        'form': form,
    })

def blog_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:blog_list')
    return render(request, 'blog/delete.html', {
        'post': post,
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