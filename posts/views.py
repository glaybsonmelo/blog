from django.db.models import Q, Count, Case, When
from django.http import request
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from comentarios.models import Comment 
from django.shortcuts import redirect, render
from comentarios.forms import FormComment
from .models import Post
from django.contrib import messages


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'pts'
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicated_post=True)
        qs = qs.annotate(
            comments_number=Count(
                Case(
                    When(comment__published_comment=True, then=1)
                )
            )
        )
        return qs


class PostSearch(PostIndex):
    template_name = 'posts/post_search.html'
    
    def get_queryset(self):
        qs =  super().get_queryset()
        termo = self.request.GET.get('termo')
    
        if not termo:
            return qs
        
        qs = qs.filter(
            Q(post_title__icontains=termo) |
            Q(author_post__first_name__iexact=termo)|
            Q(content_post__icontains=termo) |
            Q(excerpt_post__icontains=termo) |
            Q(category_post__category_name__iexact=termo)
        )
        return qs


class PostCategorie(PostIndex):
    template_name = 'posts/post_categorie.html'

    def get_queryset(self):
        qs =  super().get_queryset()
    
        categ = self.kwargs.get('categorie', None)
        print(categ)

        if not categ:
            return qs
    
        qs = qs.filter(category_post__category_name__iexact=categ)
        
        return qs


class PostDetails(UpdateView):
    template_name = 'posts/post_details.html'
    model = Post
    form_class = FormComment
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(published_comment=True,
        post_comment=post.id)

        context['comments'] = comments


        return context

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comment(**form.cleaned_data)
        comentario.post_comment = post

        if self.request.user.is_authenticated:
            comentario.user_comment = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentario enviado com sucesso.')

        return redirect('post_details', pk=post.id)
