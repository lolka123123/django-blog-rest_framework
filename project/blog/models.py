from django.db import models
from django.conf import settings

from . import validators

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль')
    views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class ArticleParagraph(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='paragraphs')
    description = models.CharField(null=True, blank=True, max_length=255, verbose_name='Описаниe')

    class Meta:
        verbose_name = 'Обзац'
        verbose_name_plural = 'Обзац'



class ArticleParagraphImage(models.Model):
    paragraph = models.ForeignKey(ArticleParagraph, on_delete=models.CASCADE, verbose_name='Параграф',
                                  related_name='images')
    image = models.ImageField(upload_to='blog/images', validators=[validators.validator_file_size],
                              verbose_name='Изображение')


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья',
                                related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль')
    text = models.CharField(max_length=255, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.profile

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


