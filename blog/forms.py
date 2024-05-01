from django import forms

from .models import Post


# Create your form here:


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'author']
