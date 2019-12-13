from django.test import SimpleTestCase, TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse, resolve
from sign_in.views import sign_in, success
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages


class TestUrls(SimpleTestCase):
    def test_sign_in_main_resolve(self):
        url = reverse('sign-in')
        self.assertEqual(resolve(url).func, sign_in)

    def test_sign_in_success_resolve(self):
        url = reverse('sign-in-success')
        self.assertEqual(resolve(url).func, success)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.authentication_url = reverse('sign-in')
        self.success_url = reverse('sign-in-success')

    def test_sign_in_success_view_GET(self):
        response = self.client.get(self.success_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_in_success.html')
        self.assertTemplateUsed(response, 'sign_in_basic.html')
        

    def test_sign_in_main_view_GET(self):
        response = self.client.get(self.authentication_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_in_main.html')
        self.assertTemplateUsed(response, 'sign_in_basic.html')

    def test_sign_in_main_view_POST_add_new_user(self):
        User.objects.create_user(username="valid_username",password="valid_password")

        response = self.client.post(self.authentication_url, {
            'username': 'valid_username',
            'password': 'valid_password'
        }, follow=True)

        messages = list(response.context['messages'])

        self.assertEquals(response.status_code, 200)
        self.assertRedirects(response, '/sign_in/success/')
        self.assertEquals(str(messages[0]), 'Successsfully signed in as valid_username')

    def test_sign_in_main_view_POST_wrong_password(self):
        response = self.client.post(self.authentication_url, {
            'username': 'valid_username',
            'password': 'wrong_password'
        }, follow=True)

        messages = list(response.context['messages'])

        self.assertEquals(response.status_code, 200)
        self.assertEquals(str(messages[0]), 'Invalid user credentials!')
