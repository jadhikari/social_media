from termios import OPOST
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostCreateForm, CommentForm
from django.contrib.auth.decorators import login_required

from .models import Post
from user.models import Profile
# Create your views here.

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            # Redirect to a success page or any other appropriate action
            return redirect('user:index')
    else:
        form = PostCreateForm(data=request.GET)
        
    return render(request, 'post/create.html', {'form': form})

@login_required
def feed(request):
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post,id=post_id)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()


    posts = Post.objects.all()
    logged_user = request.user
    return render(request, 'post/feed.html', {'posts': posts,'logged_user':logged_user,'comment_form':comment_form})


def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post,id=post_id)
    if post.like_by.filter(id =request.user.id).exists():
        post.like_by.remove(request.user)
    else:
        post.like_by.add(request.user)

    return redirect('post:post_like')