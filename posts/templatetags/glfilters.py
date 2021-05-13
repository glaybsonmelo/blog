from django import template


register = template.Library()

@register.filter(name='plural_comentarios')
def plural_comentarios(num_comment):
    try:
        num_comment = int(num_comment)
        if num_comment == 0:
            return 'Nenhum comentário'
        elif num_comment > 1:
            return f'{num_comment} comentários'
        else:
            return f'{num_comment} comentário'  
    except:
        return f'{num_comment} comentário(s)'
