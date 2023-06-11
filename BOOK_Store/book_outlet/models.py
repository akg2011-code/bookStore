from django.urls import reverse
from django.db import models
from  django.utils.text import slugify
# Create your models here.

class Book(models.Model): 
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.CharField(max_length=100, default="Unknown")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def get_absolute_url(self): 
        return reverse("book_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"

