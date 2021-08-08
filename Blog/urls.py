from django.urls import path
from . import views
from .views import BlogHomeView, BlogDetailView, AddBlogView, UpdateBlogView, DeletePostView, AddCategoryView

urlpatterns = [
    # path('', views.bloghome, name = "bloghome")
    path('', BlogHomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blog_detail"),
    path('add_post/', AddBlogView.as_view(), name = "add_post"),
    path('add_category/', AddCategoryView.as_view(), name = "add_category"),
    path('category/<slug:name>/', views.CategoryView, name="category"),
    path('update_post/edit/<int:pk>', UpdateBlogView.as_view(), name = "update_post"),
    path('delete_post/<int:pk>/delete/', DeletePostView.as_view(), name = "delete_post"),
    path('like/<int:pk>', views.LikeView, name = 'like_post'),
] 
