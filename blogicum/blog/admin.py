from django.contrib import admin

from .models import Category, Location, Post


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'category', 'is_published'
    )

    list_editabel = (
        'is_published',
    )

    list_filter = (
        'is_published', 'category'
    )


admin.site.register(Category)

admin.site.register(Location)

admin.site.register(Post, BlogAdmin)