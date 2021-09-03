from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Article
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




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



# MUST UPDATE ARTICLE CREATE IN PART 8 WHEN YOU GET THERE
# class CatCreate(CreateView):
#   model = Cat
#   fields = ['name', 'breed', 'description', 'age']
  
#   # This inherited method is called when a
#   # valid cat form is being submitted
#   def form_valid(self, form):
#     # Assign the logged in user (self.request.user)
#     form.instance.user = self.request.user  # form.instance is the cat
#     # Let the CreateView do its job as usual
#     return super().form_valid(form)

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