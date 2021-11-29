from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CommentView, LikeComment


routers = DefaultRouter()

# routers.register('comments', CommentView)


urlpatterns = [
    path('comments/', CommentView.as_view(), name="comments"),
    path('comment/like/<pk>/', LikeComment.as_view(), name="like_comment")
]
urlpatterns += routers.urls
