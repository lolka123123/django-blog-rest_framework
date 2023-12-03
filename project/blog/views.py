from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ModelViewSet

from . import serializers, models, permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    permission_classes = [permissions.IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}


class ArticleViewSet(ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_context(self):
        return {'request': self.request}

class ArticleParagraphViewSet(ModelViewSet):
    serializer_class = serializers.ArticleParagraphSerializer

    def get_queryset(self):
        return models.ArticleParagraph.objects.filter(article_id=self.kwargs['article_pk'])

    def get_permissions(self):
        article = models.Article.objects.get(id=self.kwargs['article_pk'])
        if self.request.user.id == article.profile.user.id:
            return [permissions.IsOwner()]
        return [permissions.IsAdminOrReadOnly()]

    def get_serializer_context(self):
        return {'request': self.request,
                'article_id': self.kwargs['article_pk']}

class ArticleParagraphImageViewSet(ModelViewSet):
    serializer_class = serializers.ArticleParagraphImageSerializer

    def get_queryset(self):
        return models.ArticleParagraphImage.objects.filter(paragraph_id=self.kwargs['paragraph_pk'])

    def get_permissions(self):
        article = models.Article.objects.get(id=self.kwargs['article_pk'])
        if self.request.user.id == article.profile.user.id:
            return [permissions.IsOwner()]
        return [permissions.IsAdminOrReadOnly()]

    def get_serializer_context(self):
        return {'request': self.request,
                'paragraph_id': self.kwargs['paragraph_pk']}

class ArticleCommentViewSet(ModelViewSet):
    serializer_class = serializers.ArticleCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.ArticleComment.objects.filter(article_id=self.kwargs['article_pk'])

    def get_serializer_context(self):
        profile_id = models.Profile.objects.get(user_id=self.request.user.id).id
        return {'request': self.request,
                'article_id': self.kwargs['article_pk'],
                'profile_id': profile_id}



# Create your views here.
