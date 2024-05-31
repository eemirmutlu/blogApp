from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'created_at')  # Admin panelinde gösterilecek sütunlar

# Post modelini admin paneline kaydettik
admin.site.register(Post, PostAdmin)
