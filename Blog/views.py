from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from .serializers import *


class PostViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class AuthorViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorModelSerializer



