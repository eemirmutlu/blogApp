from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')  # Admin panelinde gösterilecek sütunlar

# Post modelini admin paneline kaydettik
admin.site.register(Post, PostAdmin)

# Bir grup oluşturarak Post modelini bu gruba ekledik
admin.site.site_header = "My Blog Admin Panel"
admin.site.site_title = "My Blog Admin Panel"
admin.site.index_title = "Welcome to My Blog Admin Panel"
admin.site.register(Post)
