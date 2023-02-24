from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.viewsets import ViewSet
from . import views
from rest_framework.routers import DefaultRouter


router1 = DefaultRouter()
router1.register('book_list', views.BookViewset, basename='book_list')

router2 = DefaultRouter()
router2.register('aproval_book_request',
                 views.Aproval_Book_Request_view, basename='aproval_book_request')

router3 = DefaultRouter()
router3.register('return_rent_book', views.return_rent_book_view,
                 basename='return_rent_book')

urlpatterns = [

    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),

]
