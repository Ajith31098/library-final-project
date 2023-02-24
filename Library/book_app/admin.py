from django.contrib import admin
from book_app.models import Book, BookRequest, BookAllocation

# Register your models here.

admin.site.register(Book)
admin.site.register(BookRequest)
admin.site.register(BookAllocation)
