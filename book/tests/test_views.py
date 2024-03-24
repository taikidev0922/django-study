from rest_framework.test import APITestCase
from book.models import Book
from django.contrib.auth import get_user_model


class TestBookUpdateAPIView(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
    TARGET_URL_WITH_PK = '/api/books/{}/'
    def test_update_success(self):
        self.client.force_authenticate(user=self.user)

        book = Book.objects.create(
            title='aaa',
            price=111
        )
        params = {
            'id':book.id,
            'title':'bbb',
            'price':222
        }
        response = self.client.put(
            self.TARGET_URL_WITH_PK.format(book.id),
            params,
            format='json',
        )
        self.assertEqual(response.status_code,200)
        book = Book.objects.get(id=book.id)
        expected_json_dict = {
            'id':book.id,
            'title':'bbb',
            'price':222
        }
        self.assertJSONEqual(response.content,expected_json_dict)

