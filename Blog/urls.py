
from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
