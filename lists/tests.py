from django.test import TestCase

# Create your tests here.


from django.urls import resolve
from lists.views import home_page

class PageTest(TestCase):
    def test_root_pageview(self):
        root = resolve('/')
        self.assertEqual(root.func, home_page)