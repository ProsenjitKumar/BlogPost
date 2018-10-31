from django.contrib import admin
from .models import BlogPost


class BlogPostModelAdmin(admin.ModelAdmin):
    list_filter = ['title', 'post_date', 'slug']
    list_display = ['title', 'post_date', 'slug']
    list_per_page = 10

admin.site.register(BlogPost, BlogPostModelAdmin)
