from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST


def main(request):
    context = {
        'posts': Post.objects.order_by('-created_at')
    }
    return render(request, 'posts/main.html', context)


def home(request):
    context = {
        'posts': Post.objects.order_by('-created_at')
    }
    return render(request, 'posts/main.html', context)


def intro(request):
    return render(request, 'posts/intro.html')


def new(request):
    form = PostForm()
    return render(request, 'posts/new.html', {'form': form})


@require_POST
def create(request):
    form = PostForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
    return redirect(form.instance)


def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, 'posts/edit.html', context)


@require_POST
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    content = {
        'posts': Post.objects.order_by('-created_at')
    }
    return render(request, 'posts/main.html', content)


@require_POST
def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
    return render(request, 'posts/main.html, context')


def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    default_view_count = post.view_count
    post.view_count = default_view_count + 1
    post.save()
    context = {
        'post': post
    }
    return render(request, 'posts/show.html', context)


