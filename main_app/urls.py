from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('articles/', views.articles_index, name='articles_index'),
  path('articles/<int:article_id>/', views.articles_detail, name='articles_detail'),
]