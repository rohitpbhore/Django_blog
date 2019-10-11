from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
import datetime
from django.utils import timezone
from django.utils.text import slugify


class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'

def post_new(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.slug = slugify(post.title)
      post.published_date = timezone.now()
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm()
  return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.slug = slugify(post.title)
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)
  return render(request, 'blog/post_edit.html', {'form': form})
