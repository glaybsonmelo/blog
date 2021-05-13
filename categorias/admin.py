from django.contrib import admin
from .models import Categorie

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')

admin.site.register(Categorie, CategoryAdmin)