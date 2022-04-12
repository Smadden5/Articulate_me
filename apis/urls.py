

from django.urls import path

# from .views import ArticleList, ArticleDetail, CommentList, CommentDetail
from .views import ArticleViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', ArticleList.as_view()),
#     path('<int:pk>/', ArticleDetail.as_view()),
#     path('', CommentList.as_view()),
#     path('<int:pk>/', CommentDetail.as_view()),
# ]

router = DefaultRouter()
router.register('', ArticleViewSet, basename='articles')
router.register('', CommentViewSet, basename='comments')
# router.register('', AOCViewSet, basename='subject')
urlpatterns = router.urls