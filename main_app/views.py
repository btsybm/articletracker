from django.shortcuts import render
from django.http import HttpResponse
from .models import Article




def home(request):
  return render(request, 'home.html')

def articles_index(request):
  articles = Article.objects.all()
  return render(request, 'articles/index.html', { 'articles': articles })

def articles_detail(request, article_id):
  article = Article.objects.get(id=article_id)
  return render(request, 'articles/detail.html', { 'article': article })