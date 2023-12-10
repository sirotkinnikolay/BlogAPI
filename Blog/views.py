from django.contrib.auth import logout
from django.shortcuts import redirect
from .serializers import *


class PostViewSet(ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class AuthorViewSet(ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorModelSerializer


def your_logout_view(request):
    logout(request)
    return redirect('/api/authors/')

