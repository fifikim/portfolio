from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField()
  text = models.TextField()
  url = models.URLField(blank=True)

  def __str__(self):
    return self.title