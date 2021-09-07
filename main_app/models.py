from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
  title = models.CharField(max_length=100)
  link = models.CharField(max_length=200)
  publication = models.CharField(max_length=100, blank=True)
  date_added = models.DateTimeField('Date added', auto_now_add=True)
  date_published = models.DateField('Date published')
  body = models.TextField(max_length=60000, default='', blank=True)
  notes = models.TextField(max_length=30000, default='', blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('articles_detail', kwargs={'article_id': self.id})