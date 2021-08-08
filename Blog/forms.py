from django import forms
from .models import Category, Post

choices = Category.objects.all().values_list('category', 'category')
choice_list = []
for item in choices:
    choice_list.append(item)
# print(choice_list)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title_blog', 'author_blog', 'category', 'body', 'snippet_blog')

        widgets = {
            'title_blog': forms.TextInput(attrs={'class': 'form-control'}),
            'author_blog': forms.TextInput(attrs={'class': 'form-control', 'value': 'username', 'id': 'author_name', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet_blog': forms.Textarea(attrs={'class': 'form-control'}),
        }
