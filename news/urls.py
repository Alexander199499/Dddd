from django.urls import path, include
from .views import PostList, PostDetail, PostUpdate, PostCreate, PostDelete, ArticleCreate

urlpatterns = [
  path('', PostList.as_view(), name='post_list'),
  path('<int:pk>', PostDetail.as_view(), name='postdetail'),
  path('createPost/', PostCreate.as_view(), name='post_create'),
  path('createArticle/', ArticleCreate.as_view(), name='article_create'),
  path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
  path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

  ]