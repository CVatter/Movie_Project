from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    genreOne = models.CharField(max_length=100)
    genreTwo = models.CharField(max_length=100)
    genreThree = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.CharField(max_length=50)
    banner = models.ImageField(default='fallback.png', blank=True)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title