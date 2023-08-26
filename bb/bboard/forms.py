from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=32)

    class Meta:
        model = Post
        fields = [
            'player',
            'categoryType',
            'title',
            'text',
        ]


