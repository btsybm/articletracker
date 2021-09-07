from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request



class Home(LoginView):
  template_name = 'home.html'

@login_required
def articles_index(request):
  articles = Article.objects.filter(user=request.user)
  return render(request, 'articles/index.html', { 'articles': articles })

@login_required
def articles_detail(request, article_id):
  article = Article.objects.get(id=article_id)
  return render(request, 'articles/detail.html', { 'article': article })




def tag_visible(element):
  if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
    return False
  if isinstance(element, Comment):
    return False
  return True

def text_from_html(article):
  soup = BeautifulSoup(article, 'html.parser')
  texts = soup.findAll(text=True)
  visible_texts = filter(tag_visible, texts)  
  return u" ".join(t.strip() for t in visible_texts)

class ArticleCreate(LoginRequiredMixin, CreateView):
  model = Article
  fields = ['title', 'link', 'publication', 'date_published', 'notes']
  success_url = '/articles/'

  def form_valid(self, form):
    form.instance.user = self.request.user 

    form.instance.body = text_from_html(urllib.request.urlopen(form.instance.link).read())

    return super().form_valid(form)






class ArticleUpdate(LoginRequiredMixin, UpdateView):
  model = Article
  fields = ['title', 'publication', 'date_published', 'body', 'notes']

class ArticleDelete(LoginRequiredMixin, DeleteView):
  model = Article
  success_url = '/articles/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('articles_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)