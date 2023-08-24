from django.contrib import admin
from .models import Category, Post, Player, Comment, PostCategory


admin.site.register(Post)
admin.site.register(Player)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)

