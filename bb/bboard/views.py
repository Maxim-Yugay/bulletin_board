from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from datetime import datetime

from .forms import PostForm
from .models import Post, Player, Subscription, Category


class PostList(ListView):
    model = Post
    ordering = 'datePub'
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('bboard.add_post')
    form_class = PostForm
    raise_exception = True
    model = Post
    template_name = 'bboard/post_create.html'
    success_url = reverse_lazy('post_detail')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.player = self.request.user.player
        post.player = Post.player.get(filter(PostList(self.player)))
        post.save()
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('bboard.post_edit')
    form_class = PostForm
    model = Post
    template_name = 'bboard/post_create.html'
    success_url = reverse_lazy('posts')


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('bboard.post_delete')
    form_class = PostForm
    model = Post
    template_name = 'bboard/post_delete.html'
    success_url = reverse_lazy('posts')


class PrivatePage(ListView):
    model = Post
    ordering = 'datePub'
    template_name = 'bboard/private_room.html'
    context_object_name = 'private_room'

    # def get_queryset(self):
    #     player_post = self.queryset.filter(player=self.request.user)
    #     return player_post

def subscriptions(request):
    if request.method == "POST":
        category_id = request.objects.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(user=request.user, category=category,).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(Subscription.objects.filter(user=request.user, category=OuterRef('pk')))
    ).order_by('name')
    return render(request, 'subscriptions.html', {'categories': categories_with_subscriptions})
