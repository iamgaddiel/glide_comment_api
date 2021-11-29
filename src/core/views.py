from django.shortcuts import render
from core.models import Comment, Like
from core.serializer import CommentSerializer, LikeSerializer
from core.utils import get_random_strings
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView


class CommentView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def list(self, request):
        query_params = self.request.query_params.get('blog', None)
        if query_params is not None:
            query = self.queryset.filter(blog=query_params)
            serializer = CommentSerializer(query, many=True)
        return Response(serializer.data)
    
class LikeComment(APIView):
    def post(self, request, *args, **kwargs):

        userId = request.data.get('userId')
        comment = Comment.objects.get(pk=request.data.get('comment'))

        data = {
            'comment': request.data.get('comment'),
            'liker': userId
        }
        comment_like_serializer = LikeSerializer(data=data)
        if comment_like_serializer.is_valid():
            comment_like_serializer.save()
            comment.likes += 1
            comment.save()
            return Response(comment_like_serializer.data, status=status.HTTP_201_CREATED)
        return Response(comment_like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
