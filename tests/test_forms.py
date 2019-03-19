from django.test import TestCase

from scraper.forms import UrlForm


class TestUrlForm(TestCase):

    def test_url_form_invalid(self):
        invalid_data = {
            "url": "www.google.pl",
        }

        form = UrlForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

    def test_url_form_valid(self):
        valid_data = {
            "url": "https://www.google.pl",
        }

        form = UrlForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)
