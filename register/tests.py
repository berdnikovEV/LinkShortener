from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from register.views import register, success
from django.contrib.auth.models import User


class TestUrls(SimpleTestCase):
    def test_register_main_resolve(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_register_success_resolve(self):
        url = reverse('register-success')
        self.assertEqual(resolve(url).func, success)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.registration_url = reverse('register')
        self.success_url = reverse('register-success')

    def test_register_success_view_GET(self):
        response = self.client.get(self.success_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_success.html')
        self.assertTemplateUsed(response, 'register_basic.html')

    def test_register_main_view_GET(self):
        response = self.client.get(self.registration_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_main.html')
        self.assertTemplateUsed(response, 'register_basic.html')

    def test_register_main_view_POST_add_new_user(self):
        response = self.client.post(self.registration_url, {
            'username': 'valid_username',
            'email':'valid@email.com',
            'password': 'valid_password',
            'password_confirmation': 'valid_password' 
        })

        self.assertEquals(response.status_code, 302)
        self.assertIsInstance(User.objects.get(username='valid_username'), User)

    def test_register_main_view_POST_wrong_password_confirmation(self):
        response = self.client.post(self.registration_url, {
            'username': 'valid_username',
            'email':'valid@email.com',
            'password': 'valid_password',
            'password_confirmation': 'invalid_confirmation' 
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.all().exists(), False)

    def test_register_main_view_POST_duplicate_username(self):

        User.objects.create_user(username = "existing_username",
                                 email="unrelated@email.com",
                                 password="unrelated_password")

        response = self.client.post(self.registration_url, {
            'username': 'existing_username',
            'email':'valid@email.com',
            'password': 'valid_password',
            'password_confirmation': 'valid_password' 
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.get(username="existing_username").email, "unrelated@email.com")



