from django.contrib import admin

from .models import PostModel, AuthorModel, TopicModel


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_author', 'topic', 'post_text', 'create_at', 'update_date', 'image']


admin.site.register(PostModel, PostAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'born', 'city']


admin.site.register(AuthorModel, AuthorAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_title' ]


admin.site.register(TopicModel, TopicAdmin)
