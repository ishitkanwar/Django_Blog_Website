from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Blog.models import Post, Category
from .forms import PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.

class BlogHomeView(ListView):
    model = Post
    template_name = 'Blog/home.html'
    # cats = Category.objects.all()
    ordering = ['-post_date', '-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogHomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'Blog/detail_view.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, pk=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

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

class AddCategoryView(CreateView):
    model = Category
    template_name = 'Blog/add_category.html'
    fields = '__all__'

def CategoryView(request, name):
    queryset = Post.objects.filter(category = name.title().replace('-', ' '))
    posts = get_list_or_404(queryset)
    context = {
        'posts': posts,
        'cats': name
    }
    return render(request, 'Blog/category.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))