from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from .models import Book
from .serializers import BookSerializer, BookRequestReturnSerializer, BookRequestSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from book_app.models import Book, BookRequest, BookAllocation
from user_app.models import User
from book_app.permission import AdminOrReadOnly
from book_app.pricing import Pricing
import datetime

# Create your views here.


class BookViewset(viewsets.ModelViewSet):

    def get_queryset(self):
        return Book.objects.filter(count__gt=0)
        # return Book.objects.filter(~Q(count=0))
    serializer_class = BookSerializer

    permission_classes = [AdminOrReadOnly]
    authentication_classes = [TokenAuthentication]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def buy_request(self, request, pk=None):

        book_obj = Book.objects.get(pk=pk)
        user_obj = request.user

        if BookAllocation.objects.filter(user_id=user_obj, status=BookAllocation.Status.RENTED).exists():
            return Response({'error': 'you have already buy a book and not yet returned'})

        book_request_object = BookRequest(
            book_id=book_obj, user_id=user_obj, aproval=BookRequest.Approve.NOTAPPROVED)
        book_request_object.save()

        return Response({'Request': 'sent to the Librarian for approval'})


class Aproval_Book_Request_view(viewsets.ModelViewSet):

    queryset = BookRequest.objects.all()
    serializer_class = BookRequestSerializer

    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def rent_aproval(self, request, pk=None):

        bookrequest_object = BookRequest.objects.get(pk=pk)

        bookrequest_object.book_id.count = bookrequest_object.book_id.count - 1
        bookrequest_object.book_id.save()
        bookrequest_object.aproval = BookRequest.Approve.APPROVED
        bookrequest_object.save()

        bookallocation_object = BookAllocation(
            status=BookAllocation.Status.RENTED)
        bookallocation_object.book_id = bookrequest_object.book_id
        bookallocation_object.user_id = bookrequest_object.user_id
        bookallocation_object.save()
        return Response({'book': 'rented by the user'})


class return_rent_book_view(viewsets.ModelViewSet):

    def get_queryset(self):
        return BookAllocation.objects.filter(user_id__id=self.request.user.id)

    serializer_class = BookRequestReturnSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):

        bookallocation_object = BookAllocation.objects.get(pk=pk)

        if bookallocation_object.status == BookAllocation.Status.RETURNED:
            return Response({'note': 'this book have already returned'})

        bookallocation_object.status = BookAllocation.Status.RETURNED

        bookallocation_object.return_date = datetime.datetime.utcnow()
        bookallocation_object.book_id.count = bookallocation_object.book_id.count + 1
        bookallocation_object.book_id.save()
        bookallocation_object.save()

        fine = Pricing.calculate_price(
            bookallocation_object.rented_date, bookallocation_object.return_date)

        data = 'Book has returned and the payment for renting the book is not find' + \
            str(data)
        return Response({'success': data})
