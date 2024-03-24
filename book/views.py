from django_filters import rest_framework as filters
import logging
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import generics,viewsets


from .serializers import BookSerializer
from .models import Book

logger =  logging.getLogger(__name__)
# APIViewを継承したパターン
# class BookCreateAPIView(views.APIView):
#     def post(self,request,*args,**kwargs):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

# class BookFilter(filters.FilterSet):
#     class Meta:
#         model = Book
#         fields = '__all__'

# class BookListAPIView(views.APIView):
#     def get(self,request,*args,**kwargs):
#         filterset = BookFilter(request.query_params,queryset=Book.objects.all())
#         if not filterset.is_valid():
#             raise ValidationError(filterset.errors)
#         serializer = BookSerializer(instance=filterset.qs,many=True)
#         return Response(serializer.data)

# class BookRetrieveAPIView(views.APIView):
#     def get(self,request,pk,*args,**kwargs):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(isinstance=book)
#         return Response(serializer.data)
    
# class BookDestroyAPIView(views.APIView):
#     def delete(self,request,pk,*args,**kwargs):
#         book = Book.objects.get(pk=pk)
#         book.delete()

# 汎用APIviewを継承したパターン
# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [filters.DjangoFilterBackend]
#     filterset_fields = '__all__'

# class BookRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookCreateAPIView(generics.CreateAPIView):
#     serializer_class = BookSerializer

#     def create(self,request,*args,**kwargs):
#         response = super().create(request,*args,**kwargs)
#         logger.info("Book(id={}) created".format(response.data['id']))
#         return response

# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDestroyAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# ModelViewSetを継承したパターン
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
