from django.contrib import admin
from activity.models import Comment, Like
from django.contrib.admin import register

@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['caption', 'user', 'post', 'reply_to']

@register(Like)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']