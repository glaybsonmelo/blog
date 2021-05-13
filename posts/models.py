from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from categorias.models import Categorie

class Post(models.Model):
    post_title = models.CharField(max_length=255, verbose_name='Título')
    author_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    date_post = models.DateField(default=timezone.now, verbose_name='Data da postagem')
    content_post = models.TextField(verbose_name='Conteudo')
    excerpt_post = models.TextField(verbose_name='Excerto')
    category_post = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Cátegoria')
    image_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicated_post = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.post_title