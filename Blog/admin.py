from django.contrib.auth.admin import UserAdmin

from .models import PostModel, AuthorModel, TopicModel, User, Subscription
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_author', 'topic', 'post_text', 'create_at', 'update_date', 'image']


admin.site.register(PostModel, PostAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'born', 'city']


admin.site.register(AuthorModel, AuthorAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_title']


admin.site.register(TopicModel, TopicAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user_sub', 'author_sub']


admin.site.register(Subscription, SubscriptionAdmin)


admin.site.register(User, UserAdmin)
