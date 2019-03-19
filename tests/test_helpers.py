from django.test import TestCase
from bs4 import BeautifulSoup

from scraper.helpers import Helper


class TestHelpers(TestCase):

    class Meta:
        attrs = {'content': "słońce, plaża, morze"}

    def test_get_keywords_valid(self):
        keywords = ['słońce', 'plaża', 'morze']

        self.assertTrue(keywords == Helper.get_keywords(self.Meta()))

    def test_get_keywords_invalid(self):
        keywords = ['słońce', 'plaża', 'morze']

        self.assertFalse(keywords != Helper.get_keywords(self.Meta()))

    def test_count_keywords_in_html_valid(self):
        keywords = ['słońce', 'plaża', 'morze']
        html_str = "<html><head></head><body>plaża, morze słońce, słońce, jakiś inny testowy tekst</body></html>"

        html = BeautifulSoup(html_str, 'html')

        data = {'słońce': 2, 'plaża': 1, 'morze': 1}

        self.assertTrue(data == Helper.count_keywords_in_html(html, keywords))

    def test_count_keywords_in_html_invalid(self):
        keywords = ['słońce', 'plaża', 'morze']
        html_str = "<html><head></head><body>plaża, morze słońce, słońce, jakiś inny testowy tekst</body></html>"

        html = BeautifulSoup(html_str, 'html')

        data = {'słońce': 2, 'plaża': 1, 'morze': 1}

        self.assertFalse(data != Helper.count_keywords_in_html(html, keywords))
