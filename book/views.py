from django_filters import rest_framework as filters
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import BookSerializer
from .models import Book

class BookCreateAPIView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = '__all__'

class BookListAPIView(views.APIView):
    def get(self,request,*args,**kwargs):
        filterset = BookFilter(request.query_params,queryset=Book.objects.all())
        if not filterset.is_valid():
            raise ValidationError(filterset.errors)
        serializer = BookSerializer(instance=filterset.qs,many=True)
        return Response(serializer.data)

class BookRetrieveAPIView(views.APIView):
    def get(self,request,pk,*args,**kwargs):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(isinstance=book)
        return Response(serializer.data)
