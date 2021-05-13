from django.db.models import fields
from django.forms import ModelForm
from .models import Comment


class FormComment(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('comment_name')
        email = data.get('email_comment')
        comentarios = data.get('comment')

        if len(nome) < 4:
            self.add_error(
                'comment_name',
                'Nome precisa ter 5 caracteres ou mais.'
            )
        if not comentarios:
            self.add_error(
                'comment',
                'Comentario vazio.'
            )
    class Meta:
        model = Comment
        fields = ('comment_name', 'email_comment', 'comment')
