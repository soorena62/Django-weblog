from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from .forms import PostForm
# Create your views here:


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-modified_date')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    template_name = 'blog/create_new_post.html'
    form_class = PostForm


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_new_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts_list')


# def post_list(request):
#     posts = Post.objects.filter(status='pub').order_by('-modified_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})


# def detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#     #     print("Exception")
#     return render(request, 'blog/post_detail.html', {'post': post})


# def create_post_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/create_new_post.html', context={'form': form})


# def update_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#     return render(request, 'blog/create_new_post.html', context={'form': form})


# def delete_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/delete_post.html', context={'post': post})

