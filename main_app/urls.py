from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('articles/', views.articles_index, name='articles_index'),
  path('articles/<int:article_id>/', views.articles_detail, name='articles_detail'),
  path('accounts/signup/', views.signup, name='signup'),
  path('articles/create/', views.ArticleCreate.as_view(), name='articles_create'),
  path('articles/<int:pk>/update/', views.ArticleUpdate.as_view(), name='articles_update'),
  path('articles/<int:pk>/delete/', views.ArticleDelete.as_view(), name='articles_delete'), 
]