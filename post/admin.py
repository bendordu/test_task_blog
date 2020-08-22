from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date',)
    list_filter = ('pub_date',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-pub_date',)
