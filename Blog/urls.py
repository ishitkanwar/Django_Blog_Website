from django.urls import path
from . import views
from .views import BlogHomeView, BlogDetailView, AddBlogView, UpdateBlogView, DeletePostView

urlpatterns = [
    # path('', views.bloghome, name = "bloghome")
    path('', BlogHomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blog_detail"),
    path('add_post/', AddBlogView.as_view(), name = "add_post"),
    path('update_post/edit/<int:pk>', UpdateBlogView.as_view(), name = "update_post"),
    path('delete_post/<int:pk>/delete/', DeletePostView.as_view(), name = "delete_post"),
] 
