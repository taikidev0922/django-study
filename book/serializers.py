from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Book
from django.core.validators import RegexValidator



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price','created_at']
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=('title','price'),
                message="タイトルと価格でユニーク"
            )
        ]
        extra_kwargs = {
            'title':{
                'validators':[
                    RegexValidator(
                        regex=r'^[0-9a-zA-Z]*$',
                        message="半角英数字で入力してください"
                    )
                ]
            }
        }
    def validate_title(self,value):
        if 'Java' in value:
            raise serializers.ValidationError("Javaは含めないでください")
        return value

    def validate(sefl,data):
        title = data.get('title')
        price = data.get('price')
        if title and '薄い本' in title and price and price > 300:
            raise serializers.ValidationError("タイトルに薄い本が含まれている場合は価格は300円以下にしてください")
        return data

class BookListSerializer(serializers.ListSerializer):
    child = BookSerializer()

