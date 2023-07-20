from django.contrib import admin
from content.models import PostMedia, Post, Tag, PostTag, TaggedUser
from django.contrib.admin import register

class PostMediaInline(admin.TabularInline):
    model = PostMedia

class PostTagInline(admin.TabularInline):
    model = PostTag

class TaggedUserInline(admin.TabularInline):
    model = TaggedUser

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['caption', 'user', 'location']
    inlines = (PostMediaInline, PostTagInline, TaggedUserInline)

@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time']
