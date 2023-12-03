from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('categories', views.CategoryViewSet)

# --------------------article
router.register('articles', views.ArticleViewSet, basename='articles')

article_router = routers.NestedDefaultRouter(router, 'articles', lookup='article')

article_router.register('paragraphs', views.ArticleParagraphViewSet, basename='paragraphs')
article_paragraph_router = routers.NestedDefaultRouter(article_router, 'paragraphs', lookup='paragraph')
article_paragraph_router.register('images', views.ArticleParagraphImageViewSet, basename='images')

article_router.register('comments', views.ArticleCommentViewSet, basename='comments')
# article_comment_router = routers.NestedDefaultRouter(article_router, 'comments', lookup='comment')
# --------------------article



urlpatterns = router.urls + article_router.urls + article_paragraph_router.urls