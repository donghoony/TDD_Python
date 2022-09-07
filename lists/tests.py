from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.


from django.urls import resolve
from lists.views import home_page

class PageTest(TestCase):
    def test_root_pageview(self):
        root = resolve('/')
        self.assertEqual(root.func, home_page)

    def test_homepage_returns_html(self):
        req = HttpRequest()
        res = home_page(req)
        self.assertTrue(res.content.startswith(b"<html>"))
        self.assertIn(b"<title>To-Do lists</title>", res.content)
        self.assertTrue(res.content.endswith(b"</html>"))