from django.contrib import admin
from django.utils.html import format_html

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['id']


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_filter = ['id']



class ArticleParagraphImageInline(admin.TabularInline):
    model = models.ArticleParagraphImage

class ArticleParagraphInline(admin.TabularInline):
    model = models.ArticleParagraph
    readonly_fields = ['images']

    def images(self, instance):
        imagess = models.ArticleParagraphImage.objects.filter(paragraph=instance)
        link = ''
        for image in imagess:
            link += f'<img src="{image.image.url}" class="thumbnail">'
        return format_html(link)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    list_filter = ['id']


    inlines = [ArticleParagraphInline]

    class Media:
        css = {
            'all': ['store/style.css']
        }


@admin.register(models.ArticleParagraph)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    list_filter = ['id']

    inlines = [ArticleParagraphImageInline]

# Register your models here.
