from rest_framework.test import APITestCase
from book.models import Book
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken



class TestBookUpdateAPIView(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
    TARGET_URL_WITH_PK = '/api/books/update/{}/'
    def test_update_success(self):
        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')

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
            'id':str(book.id),
            'title':'bbb',
            'price':222,
            'created_at': book.created_at.isoformat().replace('+00:00', 'Z'),
        }
        self.assertJSONEqual(response.content,expected_json_dict)

