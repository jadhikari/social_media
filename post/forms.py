from .models import Post, Comments
from django import forms

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','image','caption']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['body','posted_by']