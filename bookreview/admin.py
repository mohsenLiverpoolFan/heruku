from django.contrib import admin

# Register your models here.
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    pass
