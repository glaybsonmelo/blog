from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comment(models.Model):
    comment_name = models.CharField(max_length=148, verbose_name='Nome')
    email_comment = models.EmailField(verbose_name='E-mail')
    comment = models.TextField(verbose_name='Comentario')
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    date_comment = models.DateTimeField(default=timezone.now)
    published_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_name