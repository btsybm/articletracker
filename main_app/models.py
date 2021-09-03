from django.db import models


class Article(models.Model):
  title = models.CharField(max_length=100)
  link = models.CharField(max_length=200)
  publication = models.CharField(max_length=100)
  date = models.DateField('Date added')
  body = models.TextField(max_length=5000)
  notes = models.TextField(max_length=3000)

  def __str__(self):
    return self.title