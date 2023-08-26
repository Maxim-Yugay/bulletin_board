from django_filters import FilterSet
from .models import Comment, Post, Reply


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'text': ['icontains']
        }


class ResponseFilter(FilterSet):
    class Meta:
        model = Reply
        fields = {
            'responseComment': ['contains']
        }