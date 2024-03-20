from django.db import models
import uuid

class Publisher(models.Model):
    class Meta:
        db_table = 'publisher'
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(verbose_name='出版社名',max_length=100,unique=True)
    created_at = models.DateTimeField(verbose_name='登録日',auto_now_add=True)

class Author(models.Model):
    class Meta:
        db_table = 'author'
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(verbose_name='著者名',max_length=100,unique=True)
    created_at = models.DateTimeField(verbose_name='登録日',auto_now_add=True)

class Book(models.Model):
    class Meta:
        db_table = 'book'

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(verbose_name='タイトル',max_length=20,unique=True)
    price = models.IntegerField(verbose_name='価格',null = True, blank=True)
    publisher = models.ForeignKey(Publisher,verbose_name='出版社',on_delete=models.CASCADE,null=True,blank=True)
    authors = models.ManyToManyField(Author,verbose_name='著者',blank=True)
    created_at = models.DateTimeField(verbose_name='登録日',auto_now_add=True)

class BookStock(models.Model):
    class Meta:
        db_table = 'book_stock'

    book = models.OneToOneField(Book,verbose_name='本',on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='在庫数',default=0)

