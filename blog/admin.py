from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


# Apply summernote to all TextField in model.
class BlogPostModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__',
    list_display = ('user', 'title', 'slug', 'publish_date', 'timestamp', 'updated')
    list_filter = ('user', 'title', 'slug', 'publish_date')
    search_fields = ('title', 'user')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostModelAdmin)