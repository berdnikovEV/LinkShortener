from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from shorten.views import shorten, success
from shorten.models import ShortenedLink
from django.contrib.auth.models import User


class TestUrls(SimpleTestCase):
    def test_register_main_resolve(self):
        url = reverse('shorten')
        self.assertEqual(resolve(url).func, shorten)

    def test_register_success_resolve(self):
        url = reverse('shorten-success')
        self.assertEqual(resolve(url).func, success)


class TestViews(TestCase):
    def setUp(self):
        User.objects.create_user('temp', 'temp@temp.com', 'pass')
        self.client = Client()
        self.client.login(username='temp', password='pass')
        self.shortening_url = reverse('shorten')
        self.success_url = reverse('shorten-success')

    def test_shorten_success_view_GET(self):
        response = self.client.get(self.success_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shorten_success.html')
        self.assertTemplateUsed(response, 'shorten_basic.html')

    def test_shorten_main_view_GET(self):
        response = self.client.get(self.shortening_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shorten_main.html')
        self.assertTemplateUsed(response, 'shorten_basic.html')

    def test_shorten_main_view_POST_add_new_link(self):
        response = self.client.post(self.shortening_url, {
            'initial_url': 'http://dummy.url',
            'url_tags': 'dummy_tag1, dummy_tag2',
            'description': 'Some text about that link'
        })

        self.assertEquals(response.status_code, 302)
        self.assertIsInstance(ShortenedLink.objects.get(initial_url='http://dummy.url'), ShortenedLink)
