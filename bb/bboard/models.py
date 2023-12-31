from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORY_CHOICES = [
        ('TANK', 'Танк'),
        ('HEALS', 'Хиллеры'),
        ('DD', 'ДД'),
        ('SELLER', 'Продавец'),
        ('GILD_MASTER', 'Гилдмастер'),
        ('QUEST_GAME', 'Квестигры'),
        ('BLACKSMITH', 'Кузнец'),
        ('TANNER', 'Кожевник'),
        ('POTION_MASTER', 'Зельевары'),
        ('SPELL_MASTER', 'Мастер заклинаний'),
]


class Player(models.Model):
    userPlayer = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.userPlayer}"


class Category(models.Model):
    name = models.CharField(max_length=24, unique=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Post(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    categoryType = models.CharField(max_length=16, choices=CATEGORY_CHOICES, default='SELLER')
    datePub = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128,)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentPlayer = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    commentCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentPlayer


class Reply(models.Model):
    replyPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Subscription(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sub')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='sub')

