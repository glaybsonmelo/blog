from comentarios.models import Comment
from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_name', 'email_comment', 
    'post_comment', 'date_comment', 'published_comment')
    list_editable = ('published_comment', )
    list_display_links = ('id', 'comment_name', 'email_comment')


admin.site.register(Comment, CommentAdmin)


