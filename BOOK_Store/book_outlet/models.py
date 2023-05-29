from django.db import models

# Create your models here.

class Book(models.Model): 
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.CharField(max_length=100, default="Unknown")
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"