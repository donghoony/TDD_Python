from django.http import HttpRequest
from django.template.loader import render_to_string
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
        self.assertTrue(res.content.strip().endswith(b"</html>"))

    def test_home_returns_correct_html(self):
        req = HttpRequest()
        res = home_page(req)
        expected_html = render_to_string("lists/home.html")
        self.assertEqual(res.content.decode(), expected_html)