from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class PostViewSet(ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class AuthorViewSet(ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorModelSerializer

