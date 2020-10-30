from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title_blog', 'author_blog', 'body', 'snippet_blog')

        widgets = {
            'title_blog': forms.TextInput(attrs={'class': 'form-control'}),
            'author_blog': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet_blog': forms.Textarea(attrs={'class': 'form-control'}),
        }
