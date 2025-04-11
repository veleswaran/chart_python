from rest_framework.routers import DefaultRouter
from .views import PostView,CommentView
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts',PostView)

router1 = DefaultRouter()
router1.register(r'comments',CommentView)

urlpatterns =[
    path("",include(router.urls)),
    path("comment/",include(router1.urls)),
]