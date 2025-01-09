from django.contrib import admin

from posts.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        'title',
        "text",
        'author',
        'create_date',
        'update_date',
    )
    list_filter = ('create_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        'author',
        'text',
        'create_date',
        'update_date',
    )
