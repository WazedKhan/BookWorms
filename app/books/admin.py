from django.contrib import admin
from books.models import Books, Category

admin.site.register(Books)
admin.site.register(Category)
