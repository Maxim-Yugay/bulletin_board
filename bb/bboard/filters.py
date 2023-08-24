from django_filters import FilterSet
from .models import Comment, Response, Post


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'text': ['icontains']
        }


class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = {
            'responseComment': ['contains']
        }