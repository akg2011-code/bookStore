from django.contrib import admin
from .models import Book

# Register your models here.

class  BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'is_bestselling')
    list_per_page = 10
    search_fields = ('title', 'author')
    list_filter = ('author', 'rating')
    list_display_links = ('title', 'author')
admin.site.register(Book, BookAdmin)