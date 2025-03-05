from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_year = models.PositiveBigIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title