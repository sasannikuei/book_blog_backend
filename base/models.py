from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    summary = models.TextField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title
