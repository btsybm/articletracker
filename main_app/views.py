from django.shortcuts import render
from django.http import HttpResponse


class Article:  
  def __init__(self, title, link, publication, date, body, notes):
    self.title = title
    self.link = link
    self.publication = publication
    self.date = date
    self.body = body
    self.notes = notes

articles = [
  Article('Florida Condo Collapse', 'https://www.nytimes.com/interactive/2021/09/01/us/miami-building-collapse.html', 'The New York Times', '', '', '' )
]




def home(request):
  return render(request, 'home.html')

def articles_index(request):
  return render(request, 'articles/index.html', { 'articles': articles })