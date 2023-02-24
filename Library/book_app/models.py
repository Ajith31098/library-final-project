from django.db import models
from user_app.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    book_pages = models.PositiveIntegerField()
    author = models.CharField(max_length=255)
    count = models.IntegerField()

    def __str__(self):
        return self.title


class BookRequest(models.Model):

    class Approve(models.TextChoices):
        APPROVED = 'approved'
        NOTAPPROVED = 'notapproved'

    book_id = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='book_detail')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_detail')
    aproval = models.CharField(max_length=50, choices=Approve.choices)

    def __str__(self):
        return self.book_id.title


class BookAllocation(models.Model):

    class Status(models.TextChoices):
        RETURNED = 'returned'
        RENTED = 'rented'

    book_id = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='book_detail_rent')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_detail_rent')
    status = models.CharField(max_length=20, choices=Status.choices)
    rented_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.book_id.title
