from .models import Comment
from django.contrib import admin

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'create_time']
    fields = ['name', 'email', 'url', 'text', 'post']


admin.site.register(Comment, CommentAdmin)
