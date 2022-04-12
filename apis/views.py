# from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth import get_user_model

from article import models
from .serializers import ArticleSerializer, CommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthorOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer
    
# class AOCViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.AOC.objects.all()
#     serializer_class = AOCSerializer
    
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class CurrentUserView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     def get_object(self):
#         return self.request.user

# class ArticleList(generics.ListCreateAPIView):
#     queryset = models.Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Article.objects.all()
#     serializer_class = ArticleSerializer
    
# class CommentList(generics.ListCreateAPIView):
#     queryset = models.Comment.objects.all()
#     serializer_class = CommentSerializer

# class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Comment.objects.all()
#     serializer_class = CommentSerializer
