from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from users.forms import CustomUserChangeForm
from .models import Post, Comment, PostLike
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    liked = False
    if request.user.is_authenticated:
        likes_count = PostLike.objects.filter(
            post_id=pk,
            user=request.user
        ).count()
        if likes_count > 0:
            liked = True

    percent = post.likes_count() / post.views * 100

    return render(
        request,
        'blog/post_detail.html',
        {'post': post, 'liked': liked, 'percent': percent}
    )

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Comentei linha abaixo pois nao quero que seja publicado
            # post.publish()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    drafts = Post.objects.filter(published_date__isnull=True).order_by('created_date')

    return render(request, 'blog/post_draft_list.html', {'posts': drafts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()

    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return redirect('post_list')

@login_required
def post_like(request, pk):
    post_like, created = PostLike.objects.get_or_create(
        post_id=pk,
        user=request.user
    )

    return redirect('post_detail', pk=pk)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()

    return redirect('post_detail', pk=comment.post.pk)

@login_required
def user_list(request):
    UserModel = get_user_model()
    users = UserModel.objects.all().order_by('birth_date')

    return render(request, 'blog/user_list.html', {'users': users})

@login_required
def user_remove(request, pk):
    UserModel = get_user_model()
    user = get_object_or_404(UserModel, pk=pk)
    user.delete()

    return redirect('user_list')

@login_required
def user_edit(request, pk):
    UserModel = get_user_model()
    user = get_object_or_404(UserModel, pk=pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'blog/user_edit.html', {'form': form})
