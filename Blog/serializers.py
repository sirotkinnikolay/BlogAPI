from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.serializers import ModelSerializer
from .models import *


class PostModelSerializer(ModelSerializer):
    user_create = serializers.HiddenField(default=None)

    class Meta:
        model = PostModel
        fields = "__all__"

    def create(self, validated_data, **kwargs):
        user = self.context['request'].user
        aut = AuthorModel.objects.get(id=self.data['post_author'])
        if user == aut.user_access:
            validated_data['user_create'] = user
        return PostModel.objects.create(**validated_data)


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = "__all__"


class TopicModelSerializer(ModelSerializer):
    class Meta:
        model = TopicModel
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
