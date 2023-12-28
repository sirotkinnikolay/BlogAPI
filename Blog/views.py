
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.viewsets import ModelViewSet
import logging
from .serializers import *




class PostViewSet(ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class AuthorViewSet(ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorModelSerializer


class SubscriptionViewSet(ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

