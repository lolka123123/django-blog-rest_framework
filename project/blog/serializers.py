from rest_framework import serializers

from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'title']

class ArticleParagraphImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleParagraphImage
        fields = ['id', 'image']

    def create(self, validated_data):
        paragraph_id = self.context['paragraph_id']
        return models.ArticleParagraphImage.objects.create(paragraph_id=paragraph_id, **validated_data)

class ArticleParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleParagraph
        fields = ['id', 'description', 'images']

    images = ArticleParagraphImageSerializer(many=True, read_only=True)

    def create(self, validated_data):
        article_id = self.context['article_id']
        return models.ArticleParagraph.objects.create(article_id=article_id, **validated_data)

class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleComment
        fields = ['id', 'profile', 'text', 'created_at', 'updated_at']

    def create(self, validated_data):
        article_id = self.context['article_id']
        profile_id = self.context['profile_id']
        return models.ArticleComment.objects.create(article_id=article_id, profile_id=profile_id, **validated_data)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['id', 'title', 'category', 'profile', 'created_at', 'updated_at', 'views', 'paragraphs', 'comments']

    paragraphs = ArticleParagraphSerializer(many=True, read_only=True)
    comments = ArticleCommentSerializer(many=True, read_only=True)

