import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from .forms import PostForm

# Create your views here.
def blog_list(request):
    return render(request, 'blog/main.html')

def crawler_new(request):

    form = PostForm()

    return render(request, 'blog/crawler.html', {
        'form': form,
    })