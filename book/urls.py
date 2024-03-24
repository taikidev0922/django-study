from django.urls import path,include
# from .views import BookListAPIView,BookCreateAPIView
# from rest_framework import routers
from .views import BookUpdateAPIView,BookListAPIView,BookDestroyAPIView

# router = routers.SimpleRouter()
# router.register('books',BookViewSet)


urlpatterns = [
    # path('books/',BookListAPIView.as_view(),name='book-list'),
    # path('books/<uuid:pk>/',BookRetrieveAPIView.as_view(),name='book-retrieve'),
    # path('books/create/',BookCreateAPIView.as_view(),name='book-create'),
    path('api/books/',BookListAPIView.as_view()),
    path('api/books/delete/<uuid:pk>/',BookDestroyAPIView.as_view(),name='book-delete'),
    # path('books/create',BookCreateAPIView.as_view())
    path('api/books/update/<uuid:pk>/',BookUpdateAPIView.as_view(),name='book-update')
    # path('api/',include(router.urls))
]

