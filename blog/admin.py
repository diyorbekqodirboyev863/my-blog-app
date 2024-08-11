from django.contrib import admin
from . import models

# Post.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['category']

# Category.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Widget.
@admin.register(models.Widget)
class WidgetAdmin(admin.ModelAdmin):
    list_display = ['title', 'post']