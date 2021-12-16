from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from Tsr import views


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Select / Drop file to upload')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')