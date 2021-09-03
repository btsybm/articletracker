from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
  title = models.CharField(max_length=100)
  link = models.CharField(max_length=200)
  publication = models.CharField(max_length=100, blank=True)
  date = models.DateField('Date added')
  body = models.TextField(max_length=5000, default='', blank=True)
  notes = models.TextField(max_length=3000, default='', blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('articles_detail', kwargs={'article_id': self.id})