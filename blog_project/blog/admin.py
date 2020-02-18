from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.

class PosrAdmin(admin.ModelAdmin):
    list_display=['title','slug', 'author', 'body', 'publish', 'created', 'updated', 'status']
    list_filter =('status','author','publish', 'created')
    search_fields =('title','body')
    date_hierarchy= 'publish'
    raw_id_fields= ('author',)
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'body','created', 'updated', 'active')
    list_filter = ('active', 'created','updated')
    search_fields = ('name', 'email','body')



admin.site.register(Post,PosrAdmin)
admin.site.register(Comment, CommentAdmin)
