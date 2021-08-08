from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title_blog = models.CharField(max_length=255)
    author_blog = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    category = models.CharField(max_length=255, default='Coding')
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    snippet_blog = models.CharField(max_length=500, default= "Add a Snippet.")

    def __str__(self):
        return self.title_blog + ' | ' + str(self.author_blog) 
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
        # could also be changed to go back to home page
        # return reverse('home')
    def total_likes(self):
        return self.likes.count()

