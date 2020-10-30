from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Blog.models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.
# def bloghome(request):
#     return render(request, 'Blog/home.html')

class BlogHomeView(ListView):
    model = Post
    template_name = 'Blog/home.html'
    ordering = ['-post_date', '-id']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'Blog/detail_view.html'

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('Blog.add_post'), name='dispatch')
class AddBlogView(CreateView):
    model = Post
    template_name = 'Blog/add_post.html'
    form_class = PostForm
    # fields = '__all__' alternate is given below
    # fields = ('title_blog', 'author_blog', 'body') 

@method_decorator(login_required, name='dispatch')
class UpdateBlogView(UpdateView):
    model = Post
    template_name = 'Blog/update_post.html'
    # fields = '__all__' alternate is given below
    fields = ('title_blog', 'body') 

class DeletePostView(DeleteView):
    model = Post
    template_name = 'Blog/delete_post.html'
    success_url = reverse_lazy('home') 