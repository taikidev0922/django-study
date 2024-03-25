from django.test import TestCase
from django.utils.timezone import localtime
from book.serializers import BookSerializer
from book.models import Book



class TestBookSerializer(TestCase):
    def test_init_valid(self):
        input_data = {
            'title':'aaa',
            'price':111,
        }
        serializer = BookSerializer(data=input_data)
        self.assertTrue(serializer.is_valid())


    def  test_init_invalid_if_title_is_blank(self):
        input_data = {
            'title':'',
            'price':111,
        }
        serializer = BookSerializer(data=input_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {'title': ['This field may not be blank.']})

    def test_output_data(self):
        book = Book.objects.create(title='aaa', price=111)
        print(book.created_at)
        serializer = BookSerializer(instance=book)
        expected_data = {
            'id':str(book.id),
            'title': book.title,
            'price': book.price,
            'created_at': book.created_at.isoformat().replace('+00:00', 'Z'),
        }
        self.assertDictEqual(serializer.data, expected_data)
