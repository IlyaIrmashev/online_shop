from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'preview', 'created_at', 'is_published', 'views_count', )
    list_filter = ('title', )
    list_per_page = 20
    ordering = ["-pk"]