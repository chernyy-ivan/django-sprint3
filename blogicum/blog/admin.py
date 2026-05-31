from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
    )
    list_editable = ('is_published',)

    list_filter = ('is_published', 'category', 'location')

    search_fields = ('title', 'text', 'author__username')

    date_hierarchy = 'pub_date'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'slug')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('name',)
