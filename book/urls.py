from django.urls import path
from .views import BookListAPIView,BookCreateAPIView,BookRetrieveAPIView

urlpatterns = [
    path('books/',BookListAPIView.as_view(),name='book-list'),
    path('books/<int:pk>/',BookRetrieveAPIView.as_view(),name='book-retrieve'),
    path('books/create',BookCreateAPIView.as_view(),name='book-create'),
]

