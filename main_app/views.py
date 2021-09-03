from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Article
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView



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

class ArticleCreate(LoginRequiredMixin, CreateView):
  model = Article
  fields = ['title', 'link', 'publication', 'date', 'notes']
  success_url = '/articles/'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
  model = Article
  fields = ['title', 'publication', 'body', 'notes']

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