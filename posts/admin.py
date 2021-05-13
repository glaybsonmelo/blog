from django.contrib import admin
# from django.contrib.admin.options import ModelAdmin
from.models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'post_title', 'author_post', 'date_post', 
    'category_post', 'publicated_post',)
    list_editable = ('publicated_post',)
    list_display_links = ('id', 'post_title',)
    summernote_fields = ('content_post', )


admin.site.register(Post, PostAdmin)
