from django.urls import path,include
# from .views import BookListAPIView,BookCreateAPIView
from rest_framework import routers
from .views import BookViewSet

router = routers.SimpleRouter()
router.register('books',BookViewSet)


urlpatterns = [
    # path('books/',BookListAPIView.as_view(),name='book-list'),
    # path('books/<int:pk>/',BookRetrieveAPIView.as_view(),name='book-retrieve'),
    # path('books/create/',BookCreateAPIView.as_view(),name='book-create'),
    # path('books/delete/<int:pk>/',BookDestroyAPIView.as_view(),name='book-delete'),
    # path('books/',BookListAPIView.as_view()),
    # path('books/create',BookCreateAPIView.as_view())
    path('api/',include(router.urls))
]

