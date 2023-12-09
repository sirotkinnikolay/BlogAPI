from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.viewsets import ModelViewSet


class PostModel(models.Model):
    post_title = models.CharField(max_length=10000, verbose_name='название поста')
    post_author = models.ForeignKey('AuthorModel', default=None, on_delete=models.CASCADE, verbose_name='автор поста')
    topic = models.ForeignKey('TopicModel', default=None, on_delete=models.CASCADE, verbose_name='тема поста')
    post_text = models.CharField(max_length=10000, verbose_name='текст поста')
    create_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    image = models.FileField(default=None, blank=True, null=True, upload_to='files/', verbose_name='фото ')
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name='создано пользователем')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class TopicModel(models.Model):
    topic_title = models.CharField(max_length=200, verbose_name='название темы')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.topic_title


class AuthorModel(models.Model):
    author_name = models.CharField(max_length=200, verbose_name='имя автора')
    born = models.DateField(max_length=100, verbose_name='дата рождения')
    city = models.CharField(max_length=100, verbose_name='город автора')
    user_access = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name='спользователь с правами доступа')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.author_name


class DataViewSet(ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(c=5)