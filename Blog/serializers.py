from rest_framework.serializers import ModelSerializer

from .models import *


class PostModelSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = "__all__"


class TopicModelSerializer(ModelSerializer):
    class Meta:
        model = TopicModel
        fields = "__all__"
